from configurations import *  # noqa
import model


class Controller:
    """Intervene with the model and fetch the view required data"""

    def __init__(self):
        self.init_model()

    def init_model(self):
        """Creates an object model to interact with"""
        self.model = model.Model()
