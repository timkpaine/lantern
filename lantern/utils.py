def in_ipynb():
    try:
        cfg = get_ipython().config
        if cfg['IPKernelApp']['parent_appname']:
            return True
        else:
            return False
    except NameError:
        return False
