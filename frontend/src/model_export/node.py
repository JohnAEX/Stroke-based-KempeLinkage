from pickle import TUPLE2
from geometry import Geometry
from linkage import Linkage

class Node(Geometry):
    
    def __init__(self, tags: list(str), location: TUPLE2[float, float]=None) -> None:
        super(tags)
        
        self.__linkages = []
        if location is not None:
            self.__x = location[0]
            self.__y = location[1]

    def add_linkage(self, linkage: Linkage) -> None:
        self.__linkages.append(linkage)
    
    def get_linkages(self) -> list(Linkage):
        return self.__linkages