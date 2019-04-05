import abc


class DITKModel(abc.ABC):
    # Any shared data strcutures or methods should be defined as part of the parent class.

    # A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.

    # The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group.

    @classmethod
    @abc.abstractmethod
    def preprocess(*args, **kwargs):
        pass

    @classmethod
    @abc.abstractmethod
    def train(*args, **kwargs):
        pass

    @classmethod
    @abc.abstractmethod
    def test(*args, **kwargs):
        pass

    @classmethod
    @abc.abstractmethod
    def predict(*args, **kwargs):
        pass

    @classmethod
    @abc.abstractmethod
    def evaluate(*args, **kwargs):
        pass
