import sympy as sy
from model_export.model import Model

class function_exporter:

    def __init__(self, function: sy.core.add.Add) -> None:
        self.__function = function
        #self.__prepare_function()
        self.draw_saxena()
    
    def __prepare_function(self) -> None:
        alpha,beta,r,x,y = sy.symbols('a b r x y')
        self.__function = self.__function.subs(r, 1)
        print(self.__function)
        model = Model()
        link_a = model.create_and_get_multiplicator_of_factor(2, "alpha")
        link_b = model.create_and_get_multiplicator_of_factor(3, "beta")
        add = model.add_angles(link_a, link_b)
        model.sanity_check()
        model.draw_linkage()
        #for key, value in self.__function.as_coefficients_dict().items():
            #print(key.args, value)
            #for arg in key.args:
                #print(arg.as_coefficients_dict().items())
            #print(dir(key))
        print(max)
        #sy.pprint(self.__function)

    def draw_saxena(self) -> None:
        linkages = []
        model = Model()
        linkages.append(model.lengthen_or_shorten_linkage_to_length(model.create_and_get_multiplicator_of_factor(1, "alpha"), 0.353553390593274))
        linkages.append(model.lengthen_or_shorten_linkage_to_length(model.create_and_get_multiplicator_of_factor(2, "alpha"), 0.25))
        linkages.append(model.lengthen_or_shorten_linkage_to_length(model.create_and_get_multiplicator_of_factor(1, "beta"), 0.353553390593274))
        linkages.append(model.lengthen_or_shorten_linkage_to_length(model.create_and_get_multiplicator_of_factor(2, "beta"), 0.25))
        linkages.append(model.lengthen_or_shorten_linkage_to_length(model.add_or_substract_half_pi_to_linkage_angle(model.create_and_get_multiplicator_of_factor(1, "alpha"), False), -0.353553390593274))
        linkages.append(model.lengthen_or_shorten_linkage_to_length(model.add_or_substract_half_pi_to_linkage_angle(model.create_and_get_multiplicator_of_factor(1, "beta"), False), -0.353553390593274))
        linkages.append(model.lengthen_or_shorten_linkage_to_length(model.add_angles(model.create_and_get_multiplicator_of_factor(1, "alpha"), model.create_and_get_multiplicator_of_factor(1, "beta")), 0.5))
        model.add_up_linkages_to_final_result(linkages)
        model.sanity_check()
        model.draw_linkage()
    
