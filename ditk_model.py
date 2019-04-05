import abc


class DITKModel(abc.ABC):
    # Any shared data strcutures or methods should be defined as part of the parent class.

    # A list of shared arguments should be defined for each of the following methods and replace (or precede) *args.

    # The output of each of the following methods should be defined clearly and shared between all methods implemented by members of the group.

    @classmethod
    @abc.abstractmethod
    def preprocess(self, *args, **kwargs):
        """
        Uses argparse() to get dataset name, output filename, data masking ratio, seed, prediction column
        and introduces missing values accordingly

        :param args:
            args.dataset: dataset to be used
            args.train_data: name of the processed file split for training
            args.test_data: name of the processed file split for testing
            args.valid_data: name of the processed file split for testing
            args.mask_ratio: percent of data to be randomly masked
            args.seed: seed of the randomizer
            args.predict_col: column used for prediction
        :param kwargs:
        :return:
            Boolean flag of operation success / failure
        """
        pass

    @classmethod
    @abc.abstractmethod
    def train(self, train_data, validation_data=None, *args, **kwargs):
        """
        Prepares the train_data and validation_data if necessary

        :param train_data: name of the training data
        :param validation_data: name of the validation data, default None
        :param args:
        :param kwargs:
        :return:
            train_data: training data in numpy form
            val_data: validation data, default None
        """
        pass

    @classmethod
    @abc.abstractmethod
    def test(self, trained_model, test_data, *args, **kwargs):
        """
        Picked up the trained model, load the test data

        :param trained_model: name of the trained model
        :param test_data: name of the test data
        :param args:
        :param kwargs:
        :return:
            model: the trained_model
            test_data: test data in numpy form
        """
        pass

    @classmethod
    @abc.abstractmethod
    def predict(self, trained_model, test_data, prediction=None, *args, **kwargs):
        """
        Run prediction on determined column, if model already loaded from test, simply return the model and test data
        along with prediction columns

        :param trained_model: name of the trained model
        :param test_data: name of the test data
        :param prediction: column name to run prediction on
        :param args:
        :param kwargs:
        :return:
            model: the trained_model
            test_data: test data in numpy form
            prediction: col data to check against prediction
        """
        pass

    @classmethod
    @abc.abstractmethod
    def evaluate(self, trained_model, input, *args, **kwargs):
        """
        Loads the trained_model and convert target input table into numpy array

        :param trained_model: name of the trained model
        :param input: name of the input table
        :param args:
        :param kwargs:
        :return:
            model: the trained_model
            data: input data in numpy array
        """
        pass
