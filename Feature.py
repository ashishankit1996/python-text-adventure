from abc import ABC, abstractmethod

class Feature(ABC):
    name = ''
    @abstractmethod
    def give(self):
        pass 
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def climb(self):
        pass
    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def examine(self):
        pass
    @abstractmethod
    def talk(self):
        pass
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def close(self):
        pass

class Door(Feature):

    _open = False

    def __init__(self, openOrClosed):
        self._open = openOrClosed

    def open(self):
        self._open = True

    def close(self):
        self._open = False


door1 = Door(True)
print(door1._open)
