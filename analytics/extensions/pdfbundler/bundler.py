from tornado import gen


def _jupyter_bundlerextension_paths():
    """Example "hello world" bundler extension"""
    return [{
        'name': 'hello_bundler',                    # unique bundler name
        'label': 'Hello Bundler',                   # human-redable menu item label
        'module_name': 'mypackage.hello_bundler',   # module containing bundle()
        'group': 'deploy'                           # group under 'deploy' or 'download' menu
    }]


def bundle_orig(handler, model):
    """Transform, convert, bundle, etc. the notebook referenced by the given
    model.

    Then issue a Tornado web response using the `handler` to redirect
    the user's browser, download a file, show a HTML page, etc. This function
    must finish the handler response before returning either explicitly or by
    raising an exception.

    Parameters
    ----------
    handler : tornado.web.RequestHandler
        Handler that serviced the bundle request
    model : dict
        Notebook model from the configured ContentManager
    """
    handler.finish('I bundled {}!'.format(model['path']))


@gen.coroutine
def bundle(handler, model):
        # simulate a long running IO op (e.g., deploying to a remote host)
        yield gen.sleep(10)

        # now respond
        handler.finish('I spent 10 seconds bundling {}!'.format(model['path']))
