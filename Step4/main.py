# %%
from md import MD
from postprocess import Plot
from potential import LJ
from atombuilder import AtomBuilder
import pandas as pd


BuilderParameter = {
    "Weight": 1.0,
    "x_num": 3,
    "y_num": 3,
    "z_num": 3,
    "a": 2,
    "type": "FCC"
}


# %%


Builder = AtomBuilder()
myatoms = Builder.BuildAtomList(BuilderParameter)
L_J = LJ(1, 1)
MDParameter = {
    "Temperature": 120,
    "CellSize": 6.1,
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
    "name": "64Atoms_Primitive_Normalized_12"
}


Plot(PlottingParameter)

print("done")


# %%
