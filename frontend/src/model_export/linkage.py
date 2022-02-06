from pickle import TUPLE2
from node import Node
from geometry import Geometry

class Linkage(Geometry):
    
    def __init__(self, node_a: Node, node_b: Node, length: float, horizontal_contraint: bool=False, tags: list(str)=[]) -> None:
        super(tags)

        self.__node_a = node_a
        self.__node_b = node_b
        self.__length = length
        self.__constraint = horizontal_contraint
        node_a.add_linkage(self)
        node_b.add_linkage(self)

    def get_nodes(self) -> TUPLE2[Node, Node]:
        return self.__node_a, self.__node_b

    def get_length(self) -> float:
        return self.__length

    def is_constrained_horizontically(self) -> bool:
        return self.__constraint