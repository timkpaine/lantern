# import os.path
import queue
# import socket
# from contextlib import closing
# from future.moves.urllib.parse import urlsplit


# def find_free_port():
#     '''https://stackoverflow.com/questions/1365265/on-localhost-how-do-i-pick-a-free-port-number'''
#     with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
#         s.bind(('', 0))
#         return s.getsockname()[1]


# def generate_sections_of_url(url):
#     path = urlsplit(url).path
#     sections = []
#     temp = ""
#     while path != '/':
#         temp = os.path.split(path)
#         path = temp[0]
#         sections.append(temp[1])
#     sections.reverse()
#     return sections


# def fqdn(type, port, rank):
#     return type + '://' + socket.getfqdn() + ':' + str(port) + '/lantern/live/api/v1/' + str(rank)


def queue_get_all(q):
    items = []
    while True:
        try:
            items.append(q.get_nowait())
        except queue.Empty:
            break
    return ','.join(items)
