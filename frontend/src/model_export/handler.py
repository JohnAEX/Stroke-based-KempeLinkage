import sympy as sy
from model_export.model import Model

class function_exporter:

    def __init__(self, function: sy.core.add.Add) -> None:
        self.__function = function
        self.__prepare_function()
    
    def __prepare_function(self) -> None:
        alpha,beta,r,x,y = sy.symbols('a b r x y')
        self.__function = self.__function.subs(r, 1)
        print(self.__function)
        model = Model()
        model.create_multiplicator_of_factor(4, "alpha")
        model.create_multiplicator_of_factor(4, "beta")
        model.sanity_check()
        #for key, value in self.__function.as_coefficients_dict().items():
            #print(key.args, value)
            #for arg in key.args:
                #print(arg.as_coefficients_dict().items())
            #print(dir(key))
        print(max)
        #sy.pprint(self.__function)