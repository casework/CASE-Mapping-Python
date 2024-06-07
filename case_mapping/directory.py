from .base import Facet
from .case import *
from .uco import *

submodules = [v for k, v in globals().items() if k[:2] != "__" and k != "Facet"]

directory: dict[str, type[Facet]] = dict()
for submodule in submodules:
    directory |= submodule.directory
