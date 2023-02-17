import numpy as np
from abc import ABCMeta
from abc import abstractmethod
from atom import Atom


class Potential(metaclass=ABCMeta):
    @abstractmethod
    def energy(self):
        pass

    @abstractmethod
    def force(self):
        pass


class LJ(Potential):
    def __init__(self, eps, delta):
        self.eps = eps
        self.delta = delta
        return None

    def energy(self, r2) -> np.array:
        pot = 4*(1/(r2**6)-1/(r2**3))
        return pot

    def force(self, r2) -> np.array:
        dvdr = (24*(r2**3)-48)/(r2**7)
        return dvdr
