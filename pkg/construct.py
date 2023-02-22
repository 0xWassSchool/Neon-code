from abc import ABCMeta, abstractmethod
from editor import Window

class IPlugin(metaclass=ABCMeta):
    @abstractmethod
    def __body__(self):
        """the body of the Plugin"""
