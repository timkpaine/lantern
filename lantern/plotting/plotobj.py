from abc import abstractmethod, ABCMeta


class BasePlot(metaclass=ABCMeta):
    def __init__(self, backend):
        pass

    @abstractmethod
    def line(self, data, **kwargs):
        pass

    @abstractmethod
    def show(self, title='', xlabel='', ylabel='', xaxis=True, yaxis=True, xticks=True, yticks=True, legend=True, grid=True, **kwargs):
        pass
