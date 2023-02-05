from system import System
from traj import Traj
from tqdm import tqdm
from typing_extensions import TypedDict


class MD:
    def __init__(self, Params):

        self.system = System(Params["Potential"], Params["Atomlist"],
                             Params["CellSize"], Params["Cutoff"], Params["Dt"])
        self.T = Params["Temperature"]  # Temperature
        self.iter = Params["Iteration"]
        self.time = 0
        self.traj = Traj(Params["Iteration"], len(Params["Atomlist"]))

    def Run(self):
        for i in tqdm(range(self.iter)):
            self.system.update_position()
            self.system.update_velocity()
            self.system.update_position()
            self.system.periodic()
            if i % 100 == 0:
                self.traj.observe(self.system, i)
