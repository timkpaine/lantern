import numpy as np
import pandas as pd
import string

from datetime import date, timedelta
from random import seed, random, sample, randint, choice
seed(1)


def _genAsciiTicker():
    return ''.join(sample(string.ascii_uppercase, randint(3, 4)))


def _genNumTicker(count=4):
    return ''.join([str(randint(0, 9)) for _ in range(count)])


def _genExchangeCode():
    return ''.join(sample(string.ascii_uppercase, randint(1, 2)))


def _genEquityTicker(country='any'):
    western = [_genAsciiTicker() + '.' + _genExchangeCode() for _ in range(10)]
    jp_hk = [_genNumTicker() + '.' + _genExchangeCode() for _ in range(5)]
    kr = [_genNumTicker(6) + '.' + _genExchangeCode() for _ in range(6)]
    if country.lower() == 'any':
        return choice(western+jp_hk+kr)
    elif country.lower() in ['jp', 'hk']:
        return choice(jp_hk)
    elif country.lower() in ['kr']:
        return choice(kr)
    else:
        return choice(western)


def getTicker(type='equity', country='any'):
    return _genEquityTicker()


def getTsData(series=2, datetime_index=True, trend=.47, volatility=1):
    random_walk = np.zeros((1000, series))
    randbase = random()
    random_walk[0] = np.array([-1*randbase*volatility if random() < trend else randbase*volatility for _ in range(series)])
    for i in range(1, 1000):
        movement = np.array([-1*random()*volatility if random() < trend else random()*volatility for _ in range(series)])
        random_walk[i] = random_walk[i-1] + movement

    ret = pd.DataFrame(random_walk, columns=['Series ' + str(x) for x in range(series)])

    if datetime_index is True:
        ret.index = np.array([date.today()-timedelta(days=1000)+timedelta(x) for x in range(1000)])
    return ret
