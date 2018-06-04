# from nbconvert.nbconvertapp import NbConvertApp
import tempfile
import subprocess


def run(to='html', in_='', out_='', post='', template='', execute=False, execute_timeout=600, new_notebook=False):
    outname = in_.rsplit('.', 1)[0] + '.' + to
    argv = []
    argv = ['python3', '-m', 'nbconvert', '--to', to]

    if execute:
        argv.extend(['--execute', '--ExecutePreprocessor.timeout=' + str(execute_timeout)])

    if template:
        argv.extend(['--template', template])

    # print('outputting to %s' % outname)

    argv.extend([in_, '--output', outname])

    if post:
        argv.extend(['--post', post])

    try:
        if new_notebook:
            if not execute:
                raise Exception('Cannot generate new notebook without rexecution')
            fp = tempfile.NamedTemporaryFile(delete=True)
            fp.write(new_notebook)
            in_ = fp.name
        else:
            fp = None

        # print(' '.join(argv))

        subprocess.call(argv)
        # NbConvertApp.launch_instance(argv)

        with open(outname, 'rb') as fp2:
            ret = fp2.read()

            if fp:
                fp.close()
            return ret

    except Exception as e:
        print(e)
        return None
