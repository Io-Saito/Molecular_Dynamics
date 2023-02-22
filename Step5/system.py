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
        self.K = 0
        for x in self.Atoms:
            self.K = self.K+np.sum(x.vel**2)/2
        return self.K/len(self.Atoms)

    def __potential_energy(self):
        self.P = 0
        for i, x in enumerate(self.Atoms):
            for j, y in enumerate(self.Atoms):
                if i == j:
                    pass
                elif i < j:
                    dp = self.__adjustCell(y.pos-x.pos)
                    r2 = np.sum((dp)**2)
                    if r2 < self.cutoff**2:
                        self.P = self.P + \
                            (self.pot.energy(r2)-self.pot.energy(self.cutoff**2))
                    else:
                        pass
                else:
                    pass
        return self.P/len(self.Atoms)

    def __adjustCell(self, dp: np.ndarray):
        halfcell = self.cellsize * 0.5
        for i in range(0, 3):
            if dp[i] < -halfcell:
                dp[i] = dp[i]+self.cellsize
            elif dp[i] > halfcell:
                dp[i] = dp[i]-self.cellsize
        return dp

    def update_velocity(self):
        for i, x in enumerate(self.Atoms):
            for j, y in enumerate(self.Atoms):
                if i == j:
                    pass
                elif i < j:
                    dp = self.__adjustCell(y.pos-x.pos)
                    r2 = np.sum((dp)**2)
                    if r2 < self.cutoff**2:
                        x.vel = x.vel + (self.pot.force(r2)*dp*self.dt)
                        y.vel = y.vel - (self.pot.force(r2)*dp*self.dt)
                    else:
                        pass
                else:
                    pass

    def update_position(self):
        for x in self.Atoms:
            x.move(self.dt)

    def periodic(self):
        for x in self.Atoms:
            x.periodic(self.cellsize)

    def total_energy(self):
        self.E = 0
        self.E = self.__kinetic_energy()+self.__potential_energy()
        return self.E
