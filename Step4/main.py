# %%
from md import MD
from postprocess import Plot
from potential import LJ
from atombuilder import AtomBuilder
import pandas as pd


BuilderParameter = {
    "Weight": 1.0,
    "x_num": 4,
    "y_num": 4,
    "z_num": 4,
    "a": 2,
    "type": "FCC"
}


# %%


Builder = AtomBuilder()
myatoms = Builder.BuildAtomList(BuilderParameter)
L_J = LJ(1, 1)
MDParameter = {
    "Temperature": 120,
    "CellSize": 8,
    "Cutoff": 2,
    "Iteration": 5000,
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
    "timestep": 5000,
    "AtomList": myatoms,
    "name": "27Atoms_BCC_Normalized_11"
}


Plot(PlottingParameter)

print("done")


# %%
