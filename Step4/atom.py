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

    def set_initial_velocity(self, vel):
        r = vel
        phi = np.random.uniform(0, 1)*2*np.pi
        theta = np.random.uniform(0, 1)*2*np.pi
        self.vel = np.array(
            [np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)])*r

    def move(self, dt):
        self.pos = self.pos+self.vel/2*dt

    def periodic(self, cellsize):
        for i in range(0, 3):
            if self.pos[i] > cellsize/2:
                self.pos[i] -= cellsize/2
            if self.pos[i] < -cellsize/2:
                self.pos[i] += cellsize/2
