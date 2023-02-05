from typing import List, Literal
from postprocess import Plot
from potential import Potential
from atom import Atom
import pandas as pd
from typing_extensions import TypedDict

class MDParameters(TypedDict):
    Temperature: float
    CellSize: float
    Cutoff: float
    Iteration: int
    Dt: float
    Potential: Potential
    Atomlist: List[Atom]


class BuilderParameters(TypedDict):
    Weights: List[float]
    x_num: int
    y_num: int
    z_num: int
    a: float
    type: Literal["BCC", "FCC", "RandomPacking"]


class PlottingParameters(TypedDict):
    df: pd.DataFrame
    atom_df: List[pd.DataFrame]
    timestep: int
    AtomList: List[Atom]
    name: str
