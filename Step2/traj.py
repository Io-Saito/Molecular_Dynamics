import numpy as np
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Traj:
    def __init__(self,iter, atom_num):
        self.df = pd.DataFrame(columns=["timestep", "E", "K", "P"])
        self.atom_traj = []
        for x in range(atom_num):
            new_atom_df = pd.DataFrame(
                columns=["p_x", "p_y", "p_z", "v_x", "v_y", "v_z"])
            self.atom_traj.append(new_atom_df)

    def observe(self, system, i):
        series = pd.Series(
            [i, system.total_energy(), system.K, system.P], index=self.df.columns)
        self.df = self.df.append(series, ignore_index=True)
        for i, x in enumerate(self.atom_traj):
            series_a = pd.Series(
                np.array([system.Atoms[i].pos.flatten(), system.Atoms[i].vel.flatten()]).flatten(), index=x.columns)
            self.atom_traj[i] = self.atom_traj[i].append(
                series_a, ignore_index=True)
