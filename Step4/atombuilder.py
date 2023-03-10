from atom import Atom
import numpy as np
from sympy.utilities.iterables import multiset_permutations
import itertools


class AtomBuilder:
    def __init__(self):
        self.Atoms = []

    def __Primitive(self, x_num, y_num, z_num, a):
        x_cor = np.linspace(-(x_num-1)/2, (x_num+1)/2, x_num, endpoint=False)*a
        y_cor = np.linspace(-(y_num-1)/2, (y_num+1)/2, y_num, endpoint=False)*a
        z_cor = np.linspace(-(z_num-1)/2, (z_num+1)/2, z_num, endpoint=False)*a
        self.cordinate = np.array(list(itertools.product(x_cor, y_cor, z_cor)))
        return self.cordinate

    def __BCC(self, x_num, y_num, z_num, a):
        x_vertex = np.arange(-(x_num-1)/2, (x_num+1)/2, 1)*a
        y_vertex = np.arange(-(y_num-1)/2, (y_num+1)/2, 1)*a
        z_vertex = np.arange(-(z_num-1)/2, (z_num+1)/2, 1)*a
        vertex = np.array(
            list(itertools.product(x_vertex, y_vertex, z_vertex)))
        x_center = (x_vertex[:-1]+x_vertex[1:]) / 2
        y_center = (y_vertex[:-1]+y_vertex[1:]) / 2
        z_center = (z_vertex[:-1]+z_vertex[1:]) / 2
        center = np.array(
            list(itertools.product(x_center, y_center, z_center)))
        self.cordinate = np.concatenate([center, vertex])
        return self.cordinate

    def __FCC(self, x_num, y_num, z_num, a):
        x_vertex = np.arange(-(x_num-1)/2, (x_num+1)/2, 1)*a
        y_vertex = np.arange(-(y_num-1)/2, (y_num+1)/2, 1)*a
        z_vertex = np.arange(-(z_num-1)/2, (z_num+1)/2, 1)*a
        x_center = (x_vertex[:-1]+x_vertex[1:]) / 2
        y_center = (y_vertex[:-1]+y_vertex[1:]) / 2
        z_center = (z_vertex[:-1]+z_vertex[1:]) / 2
        vertex = np.array(
            list(itertools.product(x_vertex, y_vertex, z_vertex)))
        center_xy = np.array(
            list(itertools.product(x_center, y_center, z_vertex)))
        center_yz = np.array(
            list(itertools.product(x_vertex, y_center, z_center)))
        center_xz = np.array(
            list(itertools.product(x_center, y_vertex, z_center)))
        self.cordinate = np.concatenate(
            [center_xy, center_yz, center_xz, vertex])
        return self.cordinate

    def BuildAtomList(self, params):
        if params["type"] == "Primitive":
            self.cordinate = self.__Primitive(
                params["x_num"], params["y_num"], params["z_num"], params["a"])

        elif params["type"] == "BCC":
            self.cordinate = self.__BCC(
                params["x_num"], params["y_num"], params["z_num"], params["a"])
        elif params["type"] == "FCC":
            self.cordinate = self.__FCC(
                params["x_num"], params["y_num"], params["z_num"], params["a"])
        else:
            print("invalid method")
        weight = params["Weight"]
        for i in range(self.cordinate.shape[0]):
            new_Atom = Atom(weight, self.cordinate[i, 0],
                            self.cordinate[i, 1], self.cordinate[i, 2])
            new_Atom.set_initial_velocity(1)
            self.Atoms.append(new_Atom)

        return self.Atoms
