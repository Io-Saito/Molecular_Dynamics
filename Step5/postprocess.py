import plotly.express as px
import io
import PIL
import numpy as np
from tqdm import tqdm
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.colors import qualitative
import plotly.io as pio


def Plot(params):
    df = params["df"]
    atom_df = params["atom_df"]
    name = params["name"]
    fig_2 = px.line(
        data_frame=df,
        x="timestep",
        y="Energy",
        color='Energy Profile',
        color_discrete_sequence=px.colors.qualitative.Plotly)

    fig_1 = px.scatter_3d(
        data_frame=atom_df,
        x="X",
        y="Y",
        z="Z",
        color='velocity',
        range_color=[0, 10],
        size_max=10,
        opacity=0.7,
        animation_frame='timestep')

    fig_1.update_layout(
        scene=dict(
            xaxis=dict(nticks=2, range=[-6, 6],),
            yaxis=dict(nticks=2, range=[-6, 6],),
            zaxis=dict(nticks=2, range=[-6, 6]),
            aspectratio=dict(x=1, y=1, z=1),
        ),
        width=800,
        height=800,
        margin=dict(r=20, l=10, b=10, t=10))

    savefig(fig_1, f"{name}_visualize")
    fig_2.write_image(f"{name}_energy.png")


def savefig(fig, name):
    frames = []

    for s, fr in enumerate(tqdm(fig.frames)):
        # set main traces to appropriate traces within plotly frame
        fig.update(data=fr.data)
        fig.layout.sliders[0].update(active=s)
    # generate image of current state
        frames.append(PIL.Image.open(io.BytesIO(fig.to_image(format="png"))))

    # create animated GIF
    frames[0].save(
        f"{name}.gif",
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=200,
        loop=0,
    )
