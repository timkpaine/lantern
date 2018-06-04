import base64
from bs4 import BeautifulSoup
from getpass import getpass
import email.encoders as encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import socket
import ssl
import time
from ..nbconvert import run
from ..hideinput.exporters import _html_no_code_email_template


def attach_parts(msg, parts):
    imgCount = 0
    for part in parts:
        if isinstance(part, (list, tuple)):
            partType, partText = part
            maintype, subtype = partType.split('/', 1)
            if maintype == 'text':
                part = MIMEText(partText, _subtype=subtype)
            elif maintype == 'image':
                imgCount += 1
                part = MIMEImage(partText, _subtype=subtype)
                part.add_header('Content-ID', '<image_{0:03d}>'.format(imgCount))
            else:
                pass
        msg.attach(part)


def send_mail(from_addr, to_addrs, message, attempts=1, retryDelaySecs=1, mailhost=('smtp.gmail.com', 587), useTLS=True, outlook=False):
    result = None
    attempts = attempts

    if mailhost is None:
        mailhost = [input('input mailhost address:'), int(input('input mailhost port:'))]

    for attempt in range(0, attempts):
        try:

            with smtplib.SMTP(mailhost[0], mailhost[1], timeout=10) as s:
                if useTLS:
                    s.starttls(context=ssl.create_default_context())
                pw = getpass('password for %s:' % from_addr)
                s.login(from_addr, pw)
                result = s.sendmail(from_addr, to_addrs, message)
        except (smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused) as e:
            time.sleep(retryDelaySecs)
            if attempt == attempts:
                raise e
        except (smtplib.SMTPException, socket.error, IOError) as e:
            time.sleep(retryDelaySecs)
            if attempt == attempts:
                raise e
    return result


def email_notebook(notebook,
                   from_user='',
                   to_user='',
                   subject='',
                   template=_html_no_code_email_template,
                   header='<h4>TEST HEADER</h4>',
                   footer='<h4>TEST FOOTER</h4>',
                   execute=False,
                   execute_timeout=100,
                   new_notebook=False,
                   postprocessor=None,
                   postprocessor_kwargs=None):

    x = run(to='html',
            in_=notebook,
            template=template,
            execute=execute,
            execute_timeout=execute_timeout,
            new_notebook=new_notebook)

    if not x:
        raise Exception('Something went wrong with NBConvert')

    msg = MIMEMultipart()
    soup = BeautifulSoup(x, 'html.parser')

    # extract imgs for outlook
    imgs = soup.find_all('img')

    # strip markdown links
    for item in soup.findAll('a', {'class': 'anchor-link'}):
        item.decompose()

    # remove dataframe table borders
    for item in soup.findAll('table', {'border': 1}):
        item['border'] = 0
        item['cellspacing'] = 0
        item['cellpadding'] = 0

    # add header and footer
    if header or footer:
        head = soup.find('div', {'class': 'header'})
        foot = soup.find('div', {'class': 'footer'})
        head.append(BeautifulSoup(header or '', 'html.parser'))
        foot.append(BeautifulSoup(footer or '', 'html.parser'))

    # attach main part
    for img in imgs:
        if not img.get('localdata'):
            continue
        # part = MIMEBase('application', 'octet-stream')
        # part.set_payload(base64.b64decode(img.get('localdata')))
        part = MIMEImage(base64.b64decode(img.get('localdata')), 'png', name=img.get('cell_id'))
        del img['localdata']
        encoders.encode_base64(part)
        # part.add_header('Content-Disposition', 'attachment', filename=img.get('cell_id'))
        part.add_header('Content-Disposition', 'inline', filename=img.get('cell_id'))
        part.add_header('Content-ID', '<%s>' % img.get('cell_id'))
        msg.attach(part)

    if postprocessor:
        if postprocessor_kwargs is None:
            postprocessor_kwargs = {}
        print('running postprocessor %s' % str(postprocessor))
        tmp = postprocessor(soup, **postprocessor_kwargs)
        if tmp is not None:
            soup = tmp

    attach_parts(msg, [('text/html', str(soup))])

    headerExtra = ''
    importance = 'Importance: Normal\r\n'

    msg_as_string = msg.as_string()

    composed = 'From: %s\r\nTo: %s\r\n' % (from_user, to_user) + \
        headerExtra + importance + \
        "Subject: %s\r\n%s" % (subject, msg_as_string)
    send_mail(from_user, to_user, composed, attempts=1, retryDelaySecs=2)
