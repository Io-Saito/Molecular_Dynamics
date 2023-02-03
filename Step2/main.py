# %%
from md import MD
from postprocess import Plot
from potential import LJ
from atom import Atom
from atombuilder import AtomBuilder

NA = 6.02e23
ev = 1.60218e-19
x_num = 3
y_num = 3
z_num = 3
# %%
weights = [1e-3/NA]*27

Builder = AtomBuilder()
list = Builder.BuildAtomList(weights, x_num, y_num, z_num, 1e-9, "BCC")

# %%
num_atoms = x_num*y_num*z_num
timestep = 1000
L_J = LJ(0.00789*ev, 0.368e-9)

MD_ = MD(120, timestep, num_atoms, L_J, list)
# MD_.add_atom(atom_list)
MD_.Run()
df = MD_.traj.df
atom_df = MD_.traj.atom_traj

Plot(df, atom_df, ev, timestep, list, "27Atoms_3")

print("done")

# %%
