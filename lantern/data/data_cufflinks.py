from cufflinks.datagen import scattergeo, \
                              choropleth, \
                              scatter, \
                              scatter3d, \
                              bubble, \
                              bubble3d, \
                              pie, \
                              heatmap, \
                              bars, \
                              ohlc, \
                              ohlcv, \
                              box, \
                              histogram, \
                              surface, \
                              sinwave, \
                              getName, \
                              lines


def getCFData(type, n_categories=5, n=100, **kwargs):
    if type == 'scatter':
        return scatter(n_categories,
                       n,
                       prefix=kwargs.get('prefix', 'category'),
                       mode=kwargs.get('mode', None))[['x', 'y', 'categories', 'text']]
    elif type == 'scatter3d':
        return scatter3d(n_categories,
                         n,
                         prefix=kwargs.get('prefix', 'category'),
                         mode=kwargs.get('mode', None))
    elif type == 'bubble':
        return bubble(n_categories,
                      n,
                      prefix=kwargs.get('prefix', 'category'),
                      mode=kwargs.get('mode', None))[['x', 'y', 'categories', 'size', 'text']]
    elif type == 'bubble3d':
        return bubble3d(n_categories,
                        n,
                        prefix=kwargs.get('prefix', 'category'),
                        mode=kwargs.get('mode', None))
    elif type == 'pie':
        return pie(n_labels=kwargs.get('n_lablels', 5),
                   mode=kwargs.get('mode', None))
    elif type == 'heatmap':
        return heatmap(n_x=kwargs.get('n_x', 5),
                       n_y=kwargs.get('n_y', 10))
    elif type == 'bars':
        return bars(n,
                    n_categories,
                    prefix=kwargs.get('prefix', 'category'),
                    columns=kwargs.get('columns', None),
                    mode=kwargs.get('mode', 'abc'))
    elif type == 'ohlc':
        return ohlc(n)
    elif type == 'ohlcv':
        return ohlcv(n)
    elif type == 'box':
        return box(n_traces=kwargs.get('n_traces', 5),
                   n=n,
                   mode=kwargs.get('mode', None))
    elif type == 'histogram':
        return histogram(n_traces=kwargs.get('n_traces', 1),
                         n=n,
                         mode=None)
    elif type == 'surface':
        return surface(n_x=kwargs.get('n_x', 20),
                       n_y=kwargs.get('n_y', 20))
    elif type == 'sinwave':
        return sinwave(n=n,
                       inc=kwargs.get('inc', .25))
    if type == 'scattergeo':
        return scattergeo()
    elif type == 'choropleth':
        return choropleth()
    elif type == 'stock':
        return getName(n=1,
                       name=kwargs.get('name', 3),
                       exchange=kwargs.get('exchange', 2),
                       columns=kwargs.get('columns', None),
                       mode=kwargs.get('mode', 'abc'))
    else:
        return lines(n_traces=kwargs.get('n_traces', 5),
                     n=n,
                     columns=kwargs.get('columns', None),
                     dateIndex=kwargs.get('dateIndex', True),
                     mode=kwargs.get('mode', None))
