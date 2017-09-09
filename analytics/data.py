from enum import Enum
from sklearn.datasets import make_blobs, \
                             make_classification, \
                             make_gaussian_quantiles, \
                             make_hastie_10_2, \
                             make_circles, \
                             make_moons

# make_multilabel_classification(n_samples=100, n_features=20, n_classes=5, n_labels=2, length=50, allow_unlabeled=True, sparse=False, return_indicator=’dense’, return_distributions=False, random_state=None)
# make_biclusters(shape, n_clusters, noise=0.0, minval=10, maxval=100, shuffle=True, random_state=None)
# make_checkerboard(shape, n_clusters, noise=0.0, minval=10, maxval=100, shuffle=True, random_state=None)
# make_regression(n_samples=100, n_features=100, n_informative=10, n_targets=1, bias=0.0, effective_rank=None, tail_strength=0.5, noise=0.0, shuffle=True, coef=False, random_state=None)
# make_friedman1(n_samples=100, n_features=10, noise=0.0, random_state=None)
# make_sparse_uncorrelated(n_samples=100, n_features=10, random_state=None)
# make_friedman2(n_samples=100, noise=0.0, random_state=None)
# make_friedman3(n_samples=100, noise=0.0, random_state=None)
# make_s_curve(n_samples=100, noise=0.0, random_state=None)
# make_swiss_roll(n_samples=100, noise=0.0, random_state=None)
# make_low_rank_matrix(n_samples=100, n_features=100, effective_rank=10, tail_strength=0.5, random_state=None)
# make_sparse_coded_signal(n_samples, n_components, n_features, n_nonzero_coefs, random_state=None)
# make_spd_matrix(n_dim, random_state=None)
# make_sparse_spd_matrix(dim=1, alpha=0.95, norm_diag=False, smallest_coef=0.1, largest_coef=0.9, random_state=None)


class Style(Enum):
    BLOBS          = 'blobs'
    CLASSIFICATION = 'classification'
    GAUSSIAN       = 'gaussian'
    HASTIE         = 'hastie'
    CIRCLES        = 'circles'
    MOONS          = 'moons'


class BlobsArgs:
    count = 100
    features = 2
    centers = 3
    cluster_std = 1.0
    center_box = (-10.0, 10.0)
    shuffle = True
    random_state = None


class ClassificationArgs:
    count = 100
    features = 20
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


class GaussianArgs:
    count = 100
    features = 2
    mean = None
    cov = 1.0
    n_classes = 3
    shuffle = True
    random_state = None


class HastieArgs:
    count = 100
    random_state = None


class CirclesArgs:
    count = 100
    shuffle = True
    noise = None
    random_state = None
    factor = 0.8


class MoonsArgs:
    count = 100
    shuffle = True
    noise = None
    random_state = None


def get_test_data(style, count=100, features=2, **kwargs):
    if isinstance(style, str):
        style = Style(style.lower())
    if style == Style.BLOBS:
        return make_blobs(count,
                          features,
                          kwargs.get('centers', 3),
                          kwargs.get('cluster_std', 1.0),
                          kwargs.get('center_box', (-10.0, 10.0)),
                          kwargs.get('shuffle', True),
                          kwargs.get('random_state', None))
    elif style == Style.CLASSIFICATION:
        return make_classification(count,
                                   features,
                                   kwargs.get('n_informative', 2),
                                   kwargs.get('n_redundant', 0),
                                   kwargs.get('n_repeated', 0),
                                   kwargs.get('n_classes', 2),
                                   kwargs.get('n_clusters_per_class', 2),
                                   kwargs.get('weights', None),
                                   kwargs.get('flip_y', 0.01),
                                   kwargs.get('class_sep', 1.0),
                                   kwargs.get('hypercube', True),
                                   kwargs.get('shift', 0.0),
                                   kwargs.get('scale', 1.0),
                                   kwargs.get('shuffle', True),
                                   kwargs.get('random_state', None))
    elif style == Style.GAUSSIAN:
        return make_gaussian_quantiles(n_samples=count,
                                       n_features=features,
                                       mean=kwargs.get('mean', None),
                                       cov=kwargs.get('cov', 1.0),
                                       n_classes=kwargs.get('n_classes', 3),
                                       shuffle=kwargs.get('shuffle', True),
                                       random_state=kwargs.get('random_state', None))
    elif style == Style.HASTIE:
        return make_hastie_10_2(count,
                                random_state=kwargs.get('random_state', None))
    elif style == Style.CIRCLES:
        return make_circles(count,
                            shuffle=True,
                            noise=None,
                            random_state=None,
                            factor=0.8)
    elif style == Style.MOONS:
        return make_moons(count,
                          shuffle=True,
                          noise=None,
                          random_state=None)


def as_dataframe(test_data):
    return 
