import sympy

class function_exporter:

    def __init__(self, function: sympy.core.add.Add) -> None:
        self.__function = function
    
    def __prepare_function(self) -> None:
        self.__function