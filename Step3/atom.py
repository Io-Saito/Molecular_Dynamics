import numpy as np
from abc import ABCMeta
from abc import abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Atom:
    def __init__(self, M, px, py, pz):
        self.pos = np.array([px, py, pz])
        self.vel = np.array([0, 0, 0])
        self.M = M  # mass

    def move(self, dt):
        self.pos = self.pos+self.vel/2*dt

    def periodic(self, cellsize):
        for i in range(0, 3):
            if self.pos[i] < 0.0:
                self.pos[i] += cellsize
            if self.pos[i] > cellsize:
                self.pos[i] -= cellsize
