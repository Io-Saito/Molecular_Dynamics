from system import System
from traj import Traj
from tqdm import tqdm


class MD:
    def __init__(self, T, iter, atom_num, pot, atoms):
        self.system = System(pot, atoms)
        self.T = T  # Temperature
        self.iter = iter
        self.time = 0
        self.traj = Traj(iter, atom_num)

    def Run(self):
        for i in tqdm(range(self.iter)):
            self.system.update_position()
            self.system.update_velocity()
            self.system.total_energy()
            self.system.update_position()
            if i % 10 == 0:
                self.traj.observe(self.system, i)
