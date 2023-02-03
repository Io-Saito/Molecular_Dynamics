import numpy as np
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from atom import Atom
from potential import LJ


class System:
    def __init__(self, pot,atoms):
        self.Atoms = atoms
        self.K = 0
        self.P = 0
        self.E = 0
        self.pot = pot  # J,m

    def kinetic_energy(self):
        for x in self.Atoms:
            self.K = self.K+np.sum(x.vel**2*x.M)/2
        return self.K

    def potential_energy(self):
        for i, x in enumerate(self.Atoms):
            for j, y in enumerate(self.Atoms):
                if i == j:
                    pass
                else:
                    self.P = self.P + self.pot.energy(x, y)
        return self.P

    def update_velocity(self):
        for i, x in enumerate(self.Atoms):
            total_force = 0
            for j, y in enumerate(self.Atoms):
                if i == j:
                    pass
                else:
                    total_force += self.pot.force(x, y)
            x.vel = x.vel+total_force

    def update_position(self):
        for x in self.Atoms:
            x.move()

    def total_energy(self):
        self.E = self.kinetic_energy()+self.potential_energy()
        return self.E
