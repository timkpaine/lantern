import queue
import ujson


def queue_get_all(q):
    items = []
    while True:
        try:
            items.append(q.get_nowait())
        except queue.Empty:
            break
    return items


def messages_to_json(lst):
    if lst and isinstance(lst[0], str):
        # already jsons:
        return '[' + ','.join(lst) + ']'
    return ujson.dumps(lst)
