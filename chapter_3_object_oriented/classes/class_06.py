# Abstract Classes - Abstract Base Class (abc) - Object Oriented Python
import os
from abc import ABC, abstractmethod

os.system('cls')

class Log(ABC):
    @abstractmethod
    def _log(self, message): ...

    def log_error(self, message):
        return self._log(f'Error: {message}')

    def log_success(self, message):
        return self._log(f'Success: {message}')
    
class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} ({self.__class__.__name__})')


class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = None
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name): ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

