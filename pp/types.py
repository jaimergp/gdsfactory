"""In programming, a factory is a function that returns an Object.

Functions are easy to understand because they have clear inputs and outputs.
Most gdsfactory functions take some inputs and return a Component object.
Some of these inputs are other functions.

- Component: Object with.
    - name
    - references to other components (x, y, rotation)
    - polygons in different layers
    - ports dictionary
- ComponentFactory: function that returns a Component.
- Route: Dictionary with 3 keys.
    - references: list of references (straights, bends and tapers)
    - ports: dict(input=PortIn, output=PortOut)
    - length: float (how long is this route)
- RouteFactory: function that returns a Route.

"""
import pathlib
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Tuple
from typing import Union

from phidl.device_layout import Path

from pp.component import Component
from pp.component import ComponentReference
from pp.cross_section import CrossSection
from pp.port import Port

Layer = Tuple[int, int]
Layers = Iterable[Layer]
Route = Dict[str, Union[List[ComponentReference], Dict[str, Port], float]]
RouteFactory = Callable[..., Route]
ComponentFactory = Callable[..., Component]
PathFactory = Callable[..., Path]
PathType = Union[str, pathlib.Path]

ComponentOrFactory = Union[ComponentFactory, Component]
ComponentOrPath = Union[PathType, Component]
ComponentOrReference = Union[Component, ComponentReference]
NameToFunctionDict = Dict[str, ComponentFactory]
Number = Union[float, int]
Coordinate = Tuple[float, float]
Coordinates = Iterable[Tuple[float, float]]
ComponentOrPath = Union[Component, PathType]
CrossSectionFactory = Callable[..., CrossSection]
CrossSectionOrFactory = Union[CrossSection, Callable[..., CrossSection]]


def get_name_to_function_dict(*functions) -> Dict[str, Callable]:
    """Returns a dict with function name as key and function as value."""
    return {func.__name__: func for func in functions}


__all__ = [
    "ComponentFactory",
    "ComponentOrFactory",
    "ComponentOrPath",
    "ComponentOrReference",
    "Coordinate",
    "Coordinates",
    "Layer",
    "Layers",
    "NameToFunctionDict",
    "Number",
    "PathType",
    "Route",
    "RouteFactory",
    "get_name_to_function_dict",
]
