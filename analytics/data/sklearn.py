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


def getSKData(style='timeseries', n_samples=1, **kwargs):
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
