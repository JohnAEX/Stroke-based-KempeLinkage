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
        link_a = model.create_and_get_multiplicator_of_factor(1, "alpha")
        link_b = model.create_and_get_multiplicator_of_factor(2, "beta")
        link_c = model.create_and_get_multiplicator_of_factor(3, "alpha")
        link_d = model.create_and_get_multiplicator_of_factor(4, "alpha")
        link_e = model.create_and_get_multiplicator_of_factor(5, "beta")
        link_f = model.create_and_get_multiplicator_of_factor(7, "alpha")
        result = model.add_up_linkages_to_final_result([link_a, link_b, link_c, link_d, link_e, link_f])
        model.sanity_check()
        model.draw_linkage()
        #for key, value in self.__function.as_coefficients_dict().items():
            #print(key.args, value)
            #for arg in key.args:
                #print(arg.as_coefficients_dict().items())
            #print(dir(key))
        print(max)
        #sy.pprint(self.__function)