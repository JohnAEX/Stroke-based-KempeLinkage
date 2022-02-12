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
        link_a = model.create_and_get_multiplicator_of_factor(2, "alpha")
        link_b = model.create_and_get_multiplicator_of_factor(3, "beta")
        add = model.add_angles(link_a, link_b)
        pi2 = model.add_half_pi_to_linkage_angle(add)
        lengthened = model.lengthen_or_shorten_linkage_to_length(pi2, 2)
        model.sanity_check()
        model.draw_linkage()
        #for key, value in self.__function.as_coefficients_dict().items():
            #print(key.args, value)
            #for arg in key.args:
                #print(arg.as_coefficients_dict().items())
            #print(dir(key))
        print(max)
        #sy.pprint(self.__function)