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

class LJ:
    def __init__(self, eps, delta):
        self.eps = eps
        self.delta = delta
        return None

    def energy(self, x: Atom, y: Atom) -> np.array:
        r = np.sqrt(np.sum((x.pos-y.pos)**2))
        del_r = self.delta/r
        pot = 4*self.eps*((del_r**12)-(del_r**6))
        return pot

    def force(self, x: Atom, y: Atom) -> np.array:
        r = np.sqrt(np.sum((x.pos-y.pos)**2))
        dvdr = 4*self.eps*(6*(self.delta**6)/r**7-12*(self.delta**12)/r**13)
        dxdydz = -dvdr*(x.pos-y.pos)/r
        return dxdydz
