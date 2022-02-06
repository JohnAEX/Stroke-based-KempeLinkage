from model_export.geometry import Geometry

class Node(Geometry):
    
    def __init__(self, tags: list[str], is_fixed: bool, location: tuple[float, float]=None) -> None:
        super().__init__(tags)
        
        self.__linkages = []
        if location is not None:
            self.__x = location[0]
            self.__y = location[1]

        self.__is_fixed = is_fixed

    def add_linkage(self, linkage) -> None:
        self.__linkages.append(linkage)
    
    def get_linkages(self):
        return self.__linkages