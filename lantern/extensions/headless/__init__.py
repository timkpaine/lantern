import os
import nbformat
import json


def list_to_cells(lst):
    '''convert list of cells to notebook form
    list should be of the form:
    [[list of strings representing python code for cell]]
    '''
    cells = '"cells": ['
    for cell in lst:
        to_add = '{"cell_type": "code", "execution_count": null, "metadata": {}, "outputs": [], "source": ["' + '\\n","'.join(cell) + '"]},'
        cells += to_add

    cells = cells[:-1] + '],'

    nb = '{' + cells + '"metadata": {"header": "HEADLESS", "kernelspec": {"display_name" : "python", "language": "", "name": "python"}, "language":"python"'

    return nbformat.writes(nbformat.reads(nb, as_version=4)).encode('utf-8')


def set_var(var, set_='""'):
    '''set var outside notebook'''
    if isinstance(set_, str):
        to_set = json.dumps(set_)
    elif isinstance(set_, dict) or isinstance(set_, list):
        try:
            to_set = json.dumps(set_)
        except ValueError:
            raise Exception('var not jsonable')
    else:
        raise Exception('var must be jsonable list or dict')

    os.environ['NBCONVERT_' + var] = to_set


def get_var(var, default='""'):
    '''get var inside notebook'''
    ret = os.environ.get('NBCONVERT_' + var)
    if ret is None:
        return default
    return json.loads(ret)
