import numpy as np
import pandas as pd
import string
import mimesis
import finance_enums
from faker import Faker
from datetime import datetime, date, timedelta
from random import seed, random, sample, randint, choice

try:
    xrange
    range = xrange
except:
    pass

seed(1)
fake = Faker()

_MIMESIS_LOCALES = ('cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fa', 'fi', 'fr', 'hu', 'is', 'it', 'ja', 'kk', 'ko', 'nl', 'no', 'pl', 'pt', 'ru', 'sv', 'tr', 'uk', 'zh')


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


def ticker(type='equity', country='any'):
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


# mimesis
def _company():
    return mimesis.Business().company()


def _companytype():
    return mimesis.Business().company_type()


def _mname(locale='en'):
    return mimesis.Person(locale).full_name()


def _occupation(locale='en'):
    return mimesis.Person(locale).occupation()


# Fakers
# names
def _name():
    return fake.name()


# locations
def _address():
    return fake.address()


def _email():
    return fake.email()


def _countrycode():
    return fake.bank_country()


def _city():
    return fake.city()


def _phone_number():
    return fake.phone_number()


def _zipcode():
    return fake.zipcode()


# other
def _currencycode():
    return fake.currency_code()


# pickers
def person(locale=None):
    if locale is None:
        locales = _MIMESIS_LOCALES
    else:
        locales = [locale]
    p = mimesis.Person(locale=choice(locales))
    gender = choice(['Male'] * 20 + ['Female'] * 21 + ['Other'])

    g = mimesis.enums.Gender.MALE if gender.lower() == 'male' else mimesis.enums.Gender.FEMALE
    first = p.name(g)
    last = p.last_name(g)

    return {
        'first_name': first,
        'last_name': last,
        'name': first + ' ' + last,  # western
        'age': p.age(),
        'gender': gender,
        'id': p.identifier(),
        'occupation': p.occupation(),
        'telephone': p.telephone(),
        'title': p.title(g),
        'username': p.username(),
        'university': p.university(),
        }


def people(count=50, locale=None):
    acc = []
    for _ in range(count):
        acc.append(person(locale))
    return pd.DataFrame(acc)


def company(exchanges=None):
    sector = choice(list(finance_enums.US_SECTORS))
    industry = choice(list(finance_enums.US_SECTORS_MAP[sector]))
    if exchanges:
        exchange = choice(exchanges)
    else:
        exchange = _genExchangeCode()

    return {
        'name': fake.company(),
        'address': _address(),
        'ticker': _genAsciiTicker(),
        'last_price': random()*100,
        'market_cap': randint(10**8, 10**11),
        'exchange': exchange,
        'ceo': _name(),
        'sector': sector,
        'industry': industry,
    }


def companies(count=1000):
    exchanges = [_genExchangeCode() for _ in range(5)]
    acc = []
    for _ in range(count):
        acc.append(company(exchanges))
    return pd.DataFrame(acc)


def currency():
    return _currencycode()


def trades(count=1000, interval='daily'):
    if interval not in ('daily', 'intraday'):
        raise Exception('interval must be in ("daily", "intraday")')
    comps = companies(100)

    acc = []
    for _ in range(count):
        row = comps.sample().to_dict(orient='records')[-1]
        row.pop('address')
        row.pop('ceo')
        row['volume'] = randint(1, 100) * 10
        row['price'] = (random()-.5)*10 + row['last_price']
        acc.append(row)
    return pd.DataFrame(acc)
