import sympy as sy

class function_exporter:

    def __init__(self, function: sy.core.add.Add) -> None:
        self.__function = function
        self.__prepare_function()
    
    def __prepare_function(self) -> None:
        alpha,beta,r,x,y = sy.symbols('a b r x y')
        self.__function = self.__function.subs(r, 1)
        print(self.__function.as_coefficients_dict())
        #sy.pprint(self.__function)