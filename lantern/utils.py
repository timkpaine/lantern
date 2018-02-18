from IPython import get_ipython


def in_ipynb():
    ip = get_ipython()
    if ip:
        cfg = ip.config
        if cfg.get('IPKernelApp', {'parent_appname': False}).get('parent_appname', False):
            return True
        return False
    return False
