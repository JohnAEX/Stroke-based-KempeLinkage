from frontend.src.model_export.geometry import Geometry
from linkage import Linkage
from node import Node
from geometry import Geometry
import math


class Model:

    
    def __init__(self, scale_factor=256) -> None:
        self.__scale_factor = scale_factor
        self.__all_geometry: list(Geometry) = []
        self.__maximum_multiplicator_alpha = 1
        self.__maximum_multiplicator_beta = 1
        a, b, c, d = self.__make_rhombus_nodes()
        self.__make_rhombus_linkages(a,b,c,d)
             


    def __pythagoras(self, a: float, b: float) -> float:
        return math.sqrt(a**2 + b**2)

    def __pythagoras(self, c: float) -> float:
        return math.sqrt(c**2 / 2)

    def __make_rhombus_nodes(self):
        a = Node(["rhombus", "origin"], (0,0))
        b = Node(["rhombus", "alpha"],(self.__pythagoras(self.__scale_factor), self.__pythagoras(self.__scale_factor)))
        c = Node(["rhombus", "beta"],(-self.__pythagoras(self.__scale_factor), self.__pythagoras(self.__scale_factor)))
        d = Node(["rhombus", "result"], (0, 2*self.__pythagoras(self.__scale_factor)))
        self.__all_geometry.extend([a,b,c,d])
        return a,b,c,d

    def __make_rhombus_linkages(self, a: Node, b: Node, c: Node, d: Node) -> None:
        self.__alpha_linkage = Linkage(["rhombus", "alpha", "1"], a, b, self.__scale_factor)
        self.__beta_linkage = Linkage(["rhombus", "beta", "1"], a, c, self.__scale_factor)
        self.__all_geometry.append(Linkage(["rhombus"], b, d, self.__scale_factor))
        self.__all_geometry.append(Linkage(["rhombus"], c, d, self.__scale_factor))
        