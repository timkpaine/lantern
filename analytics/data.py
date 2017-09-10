import numpy as np
import pandas as pd
import string

from datetime import date, timedelta
from random import seed, random, sample, randint, choice
from enum import Enum
from sklearn.datasets import make_regression, \
                             make_blobs, \
                             make_classification, \
                             make_multilabel_classification, \
                             make_gaussian_quantiles, \
                             make_hastie_10_2, \
                             make_circles, \
                             make_moons, \
                             make_biclusters, \
                             make_s_curve, \
                             make_checkerboard, \
                             make_friedman1, \
                             make_friedman2, \
                             make_friedman3

# make_swiss_roll(n_samples=100, noise=0.0, random_state=None)
# make_sparse_uncorrelated(n_samples=100, n_features=10, random_state=None)
# make_low_rank_matrix(n_samples=100, n_features=100, effective_rank=10, tail_strength=0.5, random_state=None)
# make_sparse_coded_signal(n_samples, n_components, n_features, n_nonzero_coefs, random_state=None)
# make_spd_matrix(n_dim, random_state=None)
# make_sparse_spd_matrix(dim=1, alpha=0.95, norm_diag=False, smallest_coef=0.1, largest_coef=0.9, random_state=None)
seed(1)


class Style(Enum):
    SIMPLE_TS = 'timeseries'
    REGRESSION = 'regression'
    BLOBS = 'blobs'
    CLASSIFICATION = 'classification'
    MULTILABEL = 'multilabel'
    GAUSSIAN = 'gaussian'
    HASTIE = 'hastie'
    CIRCLES = 'circles'
    MOONS = 'moons'
    BICLUSTERS = 'biclusters'
    SCURVE = 'scurve'
    CHECKER = 'checker'
    FRIEDMAN = 'friedman'
    FRIEDMAN2 = 'friedman2'
    FRIEDMAN3 = 'friedman3'


class RegressionArgs:
    n_samples = 100
    n_features = 100
    n_informative = 10
    n_targets = 1
    bias = 0.0
    effective_rank = None
    tail_strength = 0.5
    noise = 0.0
    shuffle = True
    coef = False
    random_state = None


class BlobsArgs:
    n_samples = 100
    n_features = 2
    centers = 3
    cluster_std = 1.0
    center_box = (-10.0, 10.0)
    shuffle = True
    random_state = None


class ClassificationArgs:
    n_samples = 100
    n_features = 20
    n_informative = 2
    n_redundant = 2
    n_repeated = 0
    n_classes = 2
    n_clusters_per_class = 2
    weights = None
    flip_y = 0.01
    class_sep = 1.0
    hypercube = True
    shift = 0.0
    scale = 1.0
    shuffle = True
    random_state = None


class MultilabelClassificationArgs:
    n_samples = 100
    n_features = 20
    n_classes = 5
    n_labels = 2
    length = 50
    allow_unlabeled = True
    sparse = False
    return_indicator = 'dense'
    return_distributions = False
    random_state = None


class GaussianArgs:
    n_samples = 100
    n_features = 2
    mean = None
    cov = 1.0
    n_classes = 3
    shuffle = True
    random_state = None


class HastieArgs:
    n_samples = 12000
    random_state = None


class CirclesArgs:
    n_samples = 100
    shuffle = True
    noise = None
    random_state = None
    factor = 0.8


class MoonsArgs:
    n_samples = 100
    shuffle = True
    noise = None
    random_state = None


class BiclusterArgs:
    shape = (10, 10)
    n_clusters = 4
    noise = 0.0
    minval = 10
    maxval = 100
    shuffle = True
    random_state = None


class SCurveArgs:
    n_samples = 100
    noise = 0.0
    random_state = None


class CheckerArgs:
    shape = (10, 10)
    n_clusters = 4
    noise = 0.0
    minval = 10
    maxval = 100
    shuffle = True
    random_state = None


class FriedmanArgs:
    n_samples = 100
    n_features = 10
    noise = 0.0
    random_state = None


class Friedman2Args:
    n_samples = 100
    noise = 0.0
    random_state = None


class Friedman3Args:
    n_samples = 100
    noise = 0.0
    random_state = None


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


def getTestData(style='timeseries', n_samples=1, **kwargs):
    if isinstance(style, str):
        style = Style(style.lower())
    if style == Style.REGRESSION:
        return make_regression(n_samples,
                               kwargs.get('n_features', RegressionArgs.n_features),
                               kwargs.get('n_informative', RegressionArgs.n_informative),
                               kwargs.get('n_targets', RegressionArgs.n_targets),
                               kwargs.get('bias', RegressionArgs.bias),
                               kwargs.get('effective_rank', RegressionArgs.effective_rank),
                               kwargs.get('tail_strength', RegressionArgs.tail_strength),
                               kwargs.get('noise', RegressionArgs.noise),
                               kwargs.get('shuffle', RegressionArgs.shuffle),
                               kwargs.get('coef', RegressionArgs.coef),
                               kwargs.get('random_state', RegressionArgs.random_state))
    elif style == Style.BLOBS:
        return make_blobs(n_samples,
                          kwargs.get('n_features', BlobsArgs.n_features),
                          kwargs.get('centers', BlobsArgs.centers),
                          kwargs.get('cluster_std', BlobsArgs.cluster_std),
                          kwargs.get('center_box', BlobsArgs.center_box),
                          kwargs.get('shuffle', BlobsArgs.shuffle),
                          kwargs.get('random_state', BlobsArgs.random_state))
    elif style == Style.CLASSIFICATION:
        return make_classification(n_samples,
                                   kwargs.get('n_features', ClassificationArgs.n_features),
                                   kwargs.get('n_informative', ClassificationArgs.n_informative),
                                   kwargs.get('n_redundant', ClassificationArgs.n_redundant),
                                   kwargs.get('n_repeated', ClassificationArgs.n_repeated),
                                   kwargs.get('n_classes', ClassificationArgs.n_classes),
                                   kwargs.get('n_clusters_per_class', ClassificationArgs.n_clusters_per_class),
                                   kwargs.get('weights', ClassificationArgs.weights),
                                   kwargs.get('flip_y', ClassificationArgs.flip_y),
                                   kwargs.get('class_sep', ClassificationArgs.class_sep),
                                   kwargs.get('hypercube', ClassificationArgs.hypercube),
                                   kwargs.get('shift', ClassificationArgs.shift),
                                   kwargs.get('scale', ClassificationArgs.scale),
                                   kwargs.get('shuffle', ClassificationArgs.shuffle),
                                   kwargs.get('random_state', ClassificationArgs.random_state))
    elif style == Style.MULTILABEL:
        return make_multilabel_classification(n_samples,
                                              kwargs.get('n_features', MultilabelClassificationArgs.n_features),
                                              kwargs.get('n_classes', MultilabelClassificationArgs.n_classes),
                                              kwargs.get('n_labels', MultilabelClassificationArgs.n_labels),
                                              kwargs.get('length', MultilabelClassificationArgs.length),
                                              kwargs.get('allow_unlabeled', MultilabelClassificationArgs.allow_unlabeled),
                                              kwargs.get('sparse', MultilabelClassificationArgs.sparse),
                                              kwargs.get('return_indicator', MultilabelClassificationArgs.return_indicator),
                                              kwargs.get('return_distributions', MultilabelClassificationArgs.return_distributions),
                                              kwargs.get('random_state', MultilabelClassificationArgs.random_state))
    elif style == Style.GAUSSIAN:
        return make_gaussian_quantiles(n_samples=n_samples,
                                       n_features=kwargs.get('n_features', GaussianArgs.n_features),
                                       mean=kwargs.get('mean', GaussianArgs.mean),
                                       cov=kwargs.get('cov', GaussianArgs.cov),
                                       n_classes=kwargs.get('n_classes', GaussianArgs.n_classes),
                                       shuffle=kwargs.get('shuffle', GaussianArgs.shuffle),
                                       random_state=kwargs.get('random_state', GaussianArgs.random_state))
    elif style == Style.HASTIE:
        return make_hastie_10_2(n_samples,
                                random_state=kwargs.get('random_state', HastieArgs.random_state))
    elif style == Style.CIRCLES:
        return make_circles(n_samples,
                            kwargs.get('shuffle', CirclesArgs.shuffle),
                            kwargs.get('noise', CirclesArgs.noise),
                            kwargs.get('random_state', CirclesArgs.random_state),
                            kwargs.get('factor', CirclesArgs.factor))
    elif style == Style.MOONS:
        return make_moons(n_samples,
                          kwargs.get('shuffle', MoonsArgs.shuffle),
                          kwargs.get('noise', MoonsArgs.noise),
                          kwargs.get('random_state', MoonsArgs.random_state))
    elif style == Style.BICLUSTERS:
        return make_biclusters(kwargs.get('shape', BiclusterArgs.shape),
                               kwargs.get('n_clusters', BiclusterArgs.n_clusters),
                               kwargs.get('noise', BiclusterArgs.noise),
                               kwargs.get('minval', BiclusterArgs.minval),
                               kwargs.get('maxval', BiclusterArgs.maxval),
                               kwargs.get('shuffle', BiclusterArgs.shuffle),
                               kwargs.get('random_state', BiclusterArgs.random_state))
    elif style == Style.SCURVE:
        return make_s_curve(n_samples,
                            kwargs.get('noise', SCurveArgs.noise),
                            kwargs.get('random_state', SCurveArgs.random_state))
    elif style == Style.CHECKER:
        return make_checkerboard(kwargs.get('shape', CheckerArgs.shape),
                                 kwargs.get('n_clusters', CheckerArgs.n_clusters),
                                 kwargs.get('noise', CheckerArgs.noise),
                                 kwargs.get('minval', CheckerArgs.minval),
                                 kwargs.get('maxval', CheckerArgs.maxval),
                                 kwargs.get('shuffle', CheckerArgs.shuffle),
                                 kwargs.get('random_state', CheckerArgs.random_state))
    elif style == Style.FRIEDMAN:
        return make_friedman1(n_samples,
                              kwargs.get('n_features', FriedmanArgs.n_features),
                              kwargs.get('noise', FriedmanArgs.noise),
                              kwargs.get('random_state', FriedmanArgs.random_state))
    elif style == Style.FRIEDMAN2:
        return make_friedman2(n_samples,
                              kwargs.get('noise', Friedman2Args.noise),
                              kwargs.get('random_state', Friedman2Args.random_state))
    elif style == Style.FRIEDMAN3:
        return make_friedman3(n_samples,
                              kwargs.get('noise', Friedman3Args.noise),
                              kwargs.get('random_state', Friedman3Args.random_state))


def _as_dataframe(test_data):
    return None


def cfData(type):
    if type == 'scatter':
      return scattergeo()

def scattergeo():
  """
  Returns
  """
  path=os.path.join(os.path.dirname(__file__), '../data/scattergeo.csv')
  df=pd.read_csv(path)
  del df['Unnamed: 0']
  df['text'] = df['airport'] + ' ' + df['city'] + ', ' + df['state'] + ' ' + 'Arrivals: ' + df['cnt'].astype(str)
  df=df.rename(columns={'cnt':'z','long':'lon'})
  return df

def choropleth():
  """
  Returns
  """
  path=os.path.join(os.path.dirname(__file__), '../data/choropleth.csv')
  df=pd.read_csv(path)
  del df['Unnamed: 0']
  df['z']=[np.random.randint(0,100) for _ in range(len(df))]
  return df

def scatter3d(n_categories=5,n=10,prefix='category',mode=None):
  """
  Returns a DataFrame with the required format for
  a scatter3d plot
  Parameters:
  -----------
    n_categories : int
      Number of categories
    n : int
      Number of points for each trace
    prefix : string
      Name for each trace
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  categories=[]
  for i in range(n_categories):
    categories.extend([prefix+str(i+1)]*n)
  return pd.DataFrame({'x':np.random.randn(n*n_categories),
             'y':np.random.randn(n*n_categories),
             'z':np.random.randn(n*n_categories),
             'text':getName(n*n_categories,mode=mode),
             'categories':categories})

def bubble3d(n_categories=5,n=10,prefix='category',mode=None):
  """
  Returns a DataFrame with the required format for
  a bubble3d plot
  Parameters:
  -----------
    n_categories : int
      Number of categories
    n : int
      Number of points for each trace
    prefix : string
      Name for each trace
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  categories=[]
  for i in range(n_categories):
    categories.extend([prefix+str(i+1)]*n)
  return pd.DataFrame({'x':np.random.randn(n*n_categories),
             'y':np.random.randn(n*n_categories),
             'z':np.random.randn(n*n_categories),
             'size':np.random.randint(1,100,n*n_categories),
             'text':getName(n*n_categories,mode=mode),
             'categories':categories})

def bubble(n_categories=5,n=10,prefix='category',mode=None):
  """
  Returns a DataFrame with the required format for
  a bubble plot
  Parameters:
  -----------
    n_categories : int
      Number of categories
    n : int
      Number of points for each category
    prefix : string
      Name for each category
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  categories=[]
  for i in range(n_categories):
    categories.extend([prefix+str(i+1)]*n)
  return pd.DataFrame({'x':np.random.randn(n*n_categories),
             'y':np.random.randn(n*n_categories),
             'size':np.random.randint(1,100,n*n_categories),
             'text':getName(n*n_categories,mode=mode),
             'categories':categories})

def pie(n_labels=5,mode=None):
  """
  Returns a DataFrame with the required format for
  a pie plot
  Parameters:
  -----------
    n_labels : int
      Number of labels
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  return pd.DataFrame({'values':np.random.randint(1,100,n_labels),
             'labels':getName(n_labels,mode=mode)})

def scatter(n_categories=5,n=10,prefix='category',mode=None):
  """
  Returns a DataFrame with the required format for
  a scatter plot
  Parameters:
  -----------
    n_categories : int
      Number of categories
    n : int
      Number of points for each category
    prefix : string
      Name for each category
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  categories=[]
  for i in range(n_categories):
    categories.extend([prefix+str(i+1)]*n)
  return pd.DataFrame({'x':np.random.randn(n*n_categories),
             'y':np.random.randn(n*n_categories),
             'text':getName(n*n_categories,mode=mode),
             'categories':categories})

def heatmap(n_x=5,n_y=10):
  """
  Returns a DataFrame with the required format for
  a heatmap plot
  Parameters:
  -----------
    n_x : int
      Number of x categories
    n_y : int
      Number of y categories
  """
  x=['x_'+str(_) for _ in range(n_x)]
  y=['y_'+str(_) for _ in range(n_y)]
  return pd.DataFrame(surface(n_x-1,n_y-1).values,index=x,columns=y)

def lines(n_traces=5,n=100,columns=None,dateIndex=True,mode=None):
  """
  Returns a DataFrame with the required format for
  a scatter (lines) plot
  Parameters:
  -----------
    n_traces : int
      Number of traces
    n : int
      Number of points for each trace
    columns : [str]
      List of column names
    dateIndex : bool
      If True it will return a datetime index
      if False it will return a enumerated index
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  index=pd.date_range('1/1/15',periods=n) if dateIndex else list(range(n))
  df=pd.DataFrame(np.random.randn(n,n_traces),index=index,
    columns=getName(n_traces,columns=columns,mode=mode))
  return df.cumsum()

def bars(n=3,n_categories=3,prefix='category',columns=None,mode='abc'):
  """
  Returns a DataFrame with the required format for
  a bar plot
  Parameters:
  -----------
    n : int
      Number of points for each trace
    n_categories : int
      Number of categories for each point
    prefix : string
      Name for each category
    columns : [str]
      List of column names
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  categories=[]
  if not columns:
    columns=getName(n,mode=mode)
  for i in range(n_categories):
    categories.extend([prefix+str(i+1)])
  data=dict([(x,np.random.randint(1,100,n_categories)) for x in columns])
  return pd.DataFrame(data,index=categories)

def ohlc(n=100):
  """
  Returns a DataFrame with the required format for
  a candlestick or ohlc plot
  df[['open','high','low','close']]
  Parameters:
  -----------
    n : int
      Number of ohlc points

  """
  index=pd.date_range('1/1/15',periods=n*288,freq='5min',tz='utc')
  data=np.random.randn(n*288)
  data[0]=np.array([100])
  df=pd.DataFrame(data,index=index,
    columns=['a'])
  df=df.cumsum()
  df=df.resample('1d').ohlc()
  df.index=df.index.date
  df.index=pd.to_datetime(df.index)
  return df['a']

def ohlcv(n=100):
  """
  Returns a DataFrame with the required format for
  a candlestick or ohlc plot
  df[['open','high','low','close','volume']
  Parameters:
  -----------
    n : int
      Number of ohlc points

  """
  df=ohlc()
  df['volume']=[np.random.randint(1000,10000) for _ in range(len(df))]
  return df

def box(n_traces=5,n=100,mode=None):
  """
  Returns a DataFrame with the required format for
  a box plot
  Parameters:
  -----------
    n_traces : int
      Number of traces
    n : int
      Number of points for each trace
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  df=pd.DataFrame([np.random.chisquare(np.random.randint(2,10),n_traces) for _ in range(n)],
    columns=getName(n_traces,mode=mode))
  return df

def histogram(n_traces=1,n=500,mode=None):
  """
  Returns a DataFrame with the required format for
  a box plot
  Parameters:
  -----------
    n_traces : int
      Number of traces
    n : int
      Number of points for each trace
    mode : string
      Format for each item
        'abc' for alphabet columns
        'stocks' for random stock names
  """
  df=pd.DataFrame(np.random.randn(n,n_traces)+np.random.randint(-1,2),
    columns=getName(n_traces,mode=mode))
  return df

def surface(n_x=20,n_y=20):
  """
  Returns a DataFrame with the required format for
  a surface plot
  Parameters:
  -----------
    n_x : int
      Number of points along the X axis
    n_y : int
      Number of points along the Y axis
  """
  x=[float(np.random.randint(0,100))]
  for i in range(n_x):
    x.append(x[:1][0]+np.random.randn()*np.random.randint(1,10))
  df=pd.DataFrame(x)
  for i in range(n_y):
    df[i+1]=df[i].map(lambda x:x+np.random.randn()*np.random.randint(1,10))
  return df

def sinwave(n=4,inc=.25):
  """
  Returns a DataFrame with the required format for
  a surface (sine wave) plot
  Parameters:
  -----------
    n : int
      Ranges for X and Y axis (-n,n)
    n_y : int
      Size of increment along the axis
  """
  x=np.arange(-n,n,inc)
  y=np.arange(-n,n,inc)
  X,Y=np.meshgrid(x,y)
  R = np.sqrt(X**2 + Y**2)
  Z = np.sin(R)/(.5*R)
  return pd.DataFrame(Z,index=x,columns=y)

def getName(n=1,name=3,exchange=2,columns=None,mode='abc'):
  if columns:
    if isinstance(columns,str):
      columns=[columns]
    if n != len(columns):
      raise CufflinksError("Length of column names needs to be the \n"
          "same length of traces")
  else:
    if mode is None:
      mode=get_config_file()['datagen_mode']
    if mode=='abc':
      columns=list(string.ascii_letters[:n])
    elif mode=='stocks':
      columns=[''.join(np.random.choice(list(string.ascii_uppercase),name)) + '.' + ''.join(np.random.choice(list(string.ascii_uppercase),exchange)) for _ in range(n)]
    else:
      raise CufflinksError("Unknown mode: {0}".format(mode))
  return columns

