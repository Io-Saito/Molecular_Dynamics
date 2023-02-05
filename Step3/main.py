# %%
from md import MD
from postprocess import Plot
from potential import LJ
from atombuilder import AtomBuilder
import pandas as pd


BuilderParameter = {
    "Weights": [1]*64,
    "x_num": 4,
    "y_num": 4,
    "z_num": 4,
    "a": 1,
    "type": "BCC"
}


# %%


Builder = AtomBuilder()
myatoms = Builder.BuildAtomList(BuilderParameter)
L_J = LJ(1, 1)
MDParameter = {
    "Temperature": 120,
    "CellSize": 10,
    "Cutoff": 2,
    "Iteration": 10000,
    "Dt": 0.01,
    "Potential": L_J,
    "Atomlist": myatoms
}
# %%
MD_ = MD(MDParameter)
# MD_.add_atom(atom_list)
MD_.Run()
df = MD_.traj.df
atom_df = MD_.traj.atom_traj

PlottingParameter = {
    "df": df,
    "atom_df": atom_df,
    "timestep": 10000,
    "AtomList": myatoms,
    "name": "64Atoms_BCC_Normalized_2"
}


Plot(PlottingParameter)

print("done")

# %%
