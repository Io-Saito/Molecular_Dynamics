from atom import Atom
import numpy as np
from sympy.utilities.iterables import multiset_permutations
import itertools


class AtomBuilder:
    def __init__(self):
        self.Atoms = []

    def __BCC(self, x_num, y_num, z_num, a):
        x_cor = np.linspace(-x_num/2, x_num/2, x_num)*a
        y_cor = np.linspace(-y_num/2, y_num/2, y_num)*a
        z_cor = np.linspace(-z_num/2, z_num/2, z_num)*a
        self.cordinate = np.array(list(itertools.product(x_cor, y_cor, z_cor)))
        return self.cordinate

    def BuildAtomList(self, params):
        if params["type"] == "BCC":
            self.cordinate = self.__BCC(
                params["x_num"], params["y_num"], params["z_num"], params["a"])
        else:
            print("invalid method")
        weights = params["Weights"]
        for i in range(len(weights)):
            new_Atom = Atom(weights[i], self.cordinate[i, 0],
                            self.cordinate[i, 1], self.cordinate[i, 2])
            self.Atoms.append(new_Atom)
        return self.Atoms
