from pickle import TUPLE2
from node import node
from geometry import geometry

class linkage(geometry):
    
    def __init__(self, node_a: node, node_b: node, length: float, horizontal_contraint: bool=False, tags: list(str)=[]) -> None:
        super(tags)

        self.__node_a = node_a
        self.__node_b = node_b
        self.__length = length
        self.__constraint = horizontal_contraint
        node_a.add_linkage(self)
        node_b.add_linkage(self)

    def get_nodes(self) -> TUPLE2[node, node]:
        return self.__node_a, self.__node_b

    def get_length(self) -> float:
        return self.__length

    def is_constrained_horizontically(self) -> bool:
        return self.__constraint