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

    def energy(self, r) -> np.array:
        del_r = self.delta/r
        pot = 4*self.eps*((del_r**12)-(del_r**6))
        return pot

    def force(self,r) -> np.array:
        dvdr = 4*self.eps*(6*(self.delta**6)/r**7-12*(self.delta**12)/r**13)
        dxdydz = -dvdr/r
        return dxdydz
