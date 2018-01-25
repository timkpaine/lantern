from .base import run
from .sources.websocket import WebSocketSource
from ..utils import in_ipynb

if in_ipynb():
    print('install lanternlive')
    from IPython import get_ipython

    def foo(*args, **kwargs):
        import pdb
        pdb.set_trace()
    get_ipython().kernel.comm_manager.register_target('lanternlive', foo)
