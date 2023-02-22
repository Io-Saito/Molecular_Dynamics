import numpy as np
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Traj:
    def __init__(self, iter, atom_num):
        self.df = pd.DataFrame(columns=["timestep", "Energy Profile", "Energy"])
        self.atom_traj = pd.DataFrame(
            columns=["timestep", "atom", "X", "Y", "Z", "velocity"])

    def observe(self, system, i):

        series_P = pd.Series(
            [i, "Potential Energy", system.P], index=self.df.columns)
        series_K = pd.Series(
            [i, "Kinetic Energy", system.K], index=self.df.columns)
        series_E = pd.Series(
            [i, "Total", system.total_energy()], index=self.df.columns)
        self.df = self.df.append(
            [series_P, series_E, series_K], ignore_index=True)
        for k in range(len(system.Atoms)):
            series_a = pd.Series([i, k] +
                                 system.Atoms[k].pos.tolist() + [np.sum(system.Atoms[k].vel**2)], index=self.atom_traj.columns)
            self.atom_traj = self.atom_traj.append(
                series_a, ignore_index=True)
