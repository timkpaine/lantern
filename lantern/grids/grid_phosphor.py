
def phosphor_grid(data, **kwargs):
    from IPython.display import display
    bundle = {}
    bundle['text/csv'] = data.reset_index().to_csv()
    return display(bundle, raw=True)
