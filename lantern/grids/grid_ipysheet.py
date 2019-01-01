import ipysheet
import pandas as pd


def ipysheet_grid(data, indexed=True):
    if isinstance(data, list):
        data = pd.DataFrame(data)
        drop_index = False
    elif isinstance(data, dict):
        data = pd.DataFrame(data)
        drop_index = False
    else:
        drop_index = True

    if isinstance(data, pd.DataFrame):
        if 'index' not in data.columns and drop_index:
            data = data.reset_index()
        for x in data.dtypes.iteritems():
            if 'date' in str(x[1]):
                data[x[0]] = data[x[0]].astype(str)
    elif isinstance(data, pd.Series):
        data = data.reset_index()
        for x in data.dtypes.iteritems():
            if 'date' in str(x[1]):
                data[x[0]] = data[x[0]].astype(str)
    else:
        raise NotImplementedError()

    sheet = ipysheet.sheet(rows=len(data), columns=len(data.columns), column_headers=data.columns.astype(str).tolist())
    for i, col in enumerate(data.columns):
        ipysheet.column(i, data[col].values.tolist())
    return sheet
