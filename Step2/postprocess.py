import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Plot(df, atom_df, ev, timestep, atom_list, name):

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
        plt.rcParams['font.family'] = 'sans-serif'  # 使用するフォント
        # x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
        plt.rcParams['xtick.direction'] = 'in'
        # y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
        plt.rcParams['ytick.direction'] = 'in'
        plt.rcParams['xtick.major.width'] = 1.0  # x軸主目盛り線の線幅
        plt.rcParams['ytick.major.width'] = 1.0  # y軸主目盛り線の線幅
        plt.rcParams['font.size'] = 25  # フォントの大きさ
        plt.rcParams['axes.linewidth'] = 1.0  # 軸の線幅edge linewidth。囲みの太さ

        t.append(df["timestep"].loc[i])
        K.append(df["K"].loc[i]/ev)
        V.append(df["E"].loc[i]/ev)
        P.append(df["P"].loc[i]/ev)
        energy.plot(t, K, label='Kinetic energy', linewidth=10, c="violet")
        energy.plot(t, P, label='Potential energy', linewidth=10, c="orange")
        energy.plot(t, V, label='Total energy', linewidth=10, c="greenyellow")
        energy.set_xlim(0, timestep)
        for y in range(len(atom_list)):
            pos = atom_df[y].loc[i]
            cordinate.scatter(pos["p_x"]/1e-9, pos["p_y"] /
                              1e-9, pos["p_z"]/1e-9, s=500, c="turquoise")
        cordinate.set_xlim(-2.1, 2.1)
        cordinate.set_ylim(-2.1, 2.1)
        cordinate.set_zlim(-2.1, 2.1)
        cordinate.set_xlabel('X [nm]')
        cordinate.set_ylabel('Y [nm]')
        cordinate.set_zlabel('Z [nm]')
        cordinate.set_title('Visualization')
        energy.set_xlabel('timestep')
        energy.set_ylabel('energy')
        energy.legend(loc='upper right')
        energy.set_title('Energy [eV]')
        cordinate.set_title('Visualization')

    ani = FuncAnimation(fig, run, frames=500, interval=10, repeat=False)
    ani.save(f"./data/{name}.gif")
