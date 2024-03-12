from .base import FacetEntity
from .case import *
from .uco import *

submodules = [v for k, v in globals().items() if k[:2] != "__" and k != "FacetEntity"]

directory: dict[str, type[FacetEntity]] = dict()
for submodule in submodules:
    directory |= submodule.directory
