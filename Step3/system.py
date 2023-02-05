import numpy as np
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from atom import Atom
from potential import LJ


class System:
    def __init__(self, pot, atoms, cellsize, cutoff, dt):
        self.Atoms = atoms
        self.cellsize = cellsize
        self.cutoff = cutoff
        self.K = 0
        self.P = 0
        self.E = 0
        self.pot = pot  # J,m
        self.dt = dt

    def __kinetic_energy(self):
        for x in self.Atoms:
            self.K = self.K+np.sum(x.vel**2*x.M)/2
        return self.K

    def __potential_energy(self):
        for i, x in enumerate(self.Atoms):
            for j, y in enumerate(self.Atoms):
                if i == j:
                    pass
                else:
                    r = np.sum((x.pos-y.pos)**2)
                    if r < self.cutoff**2:
                        self.P = self.P + self.pot.energy(r)/2
                    else:
                        pass
        return self.P

    def __adjustCell(self, dp: np.ndarray):
        halfcell = self.cellsize * 0.5
        for i in range(0, 3):
            if dp[i] < -halfcell:
                dp = dp+self.cellsize
            elif dp[i] > halfcell:
                dp = dp-self.cellsize
        return dp

    def update_velocity(self):
        for i, x in enumerate(self.Atoms):
            total_force = np.array([0, 0, 0])
            for j, y in enumerate(self.Atoms):
                if i == j:
                    pass
                else:
                    dp = self.__adjustCell(x.pos-y.pos)
                    r = np.sum((dp)**2)
                    if r < self.cutoff**2:
                        total_force = total_force + self.pot.force(r)*dp
                    else:
                        pass
            x.vel = x.vel+total_force*self.dt

    def update_position(self):
        for x in self.Atoms:
            x.move(self.dt)

    def total_energy(self):
        self.E = self.__kinetic_energy()+self.__potential_energy()
        return self.E
