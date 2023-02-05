import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Plot(params):
    df = params["df"]
    atom_df = params["atom_df"]
    timestep = params["timestep"]
    atom_list = params["AtomList"]
    name = params["name"]
    fig = plt.figure(figsize=(36, 16))
    energy = fig.add_subplot(121)
    cordinate = fig.add_subplot(122, projection='3d')

    t = []
    P = []
    K = []
    V = []

    def run(i):
        cordinate.clear()
        energy.clear()
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['xtick.major.width'] = 1.0
        plt.rcParams['ytick.major.width'] = 1.0
        plt.rcParams['font.size'] = 25
        plt.rcParams['axes.linewidth'] = 1.0

        t.append(df["timestep"].loc[i])
        K.append(df["K"].loc[i])
        V.append(df["E"].loc[i])
        P.append(df["P"].loc[i])
        energy.plot(t, K, label='Kinetic energy', linewidth=10, c="violet")
        energy.plot(t, P, label='Potential energy', linewidth=10, c="orange")
        energy.plot(t, V, label='Total energy', linewidth=10, c="greenyellow")
        energy.set_xlim(0, timestep)
        for y in range(len(atom_list)):
            pos = atom_df[y].loc[i]
            cordinate.scatter(pos["p_x"], pos["p_y"],
                              pos["p_z"], s=500, c="turquoise")
        cordinate.set_xlim(-5, 5)
        cordinate.set_ylim(-5, 5)
        cordinate.set_zlim(-5, 5)
        cordinate.set_xlabel('X ')
        cordinate.set_ylabel('Y ')
        cordinate.set_zlabel('Z ')
        cordinate.set_title('Visualization')
        energy.set_xlabel('timestep')
        energy.set_ylabel('energy')
        energy.legend(loc='upper right')
        energy.set_title('Energy [eV]')
        cordinate.set_title('Visualization')

    ani = FuncAnimation(
        fig, run, frames=int(params["timestep"]/10), interval=10, repeat=False)
    ani.save(f"./data/{name}.gif")
