from frontend.src.model_export.geometry import geometry
from linkage import linkage

class node(geometry):
    
    def __init__(self, tags: list(str)) -> None:
        super(tags)
        
        self.__linkages = []

    def add_linkage(self, linkage: linkage) -> None:
        self.__linkages.append(linkage)
    
    def get_linkages(self) -> list(linkage):
        return self.__linkages