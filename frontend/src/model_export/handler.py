import sympy as sy
from model_export.model import Model

class function_exporter:

    def __init__(self, function: sy.core.add.Add) -> None:
        self.__function = function
        self.__prepare_function()
        #self.draw_saxena()
    
    def __prepare_function(self) -> None:
        r = sy.symbols('r')
        self.__function = self.__function.subs(r, 1)
        print(self.__function)
        linkages = []
        model = Model()
        for key, value in self.__function.as_coefficients_dict().items():
            if key == 1:
                continue
            linkages.append(model.lengthen_or_shorten_linkage_to_length(self.__get_linkage_for_component(key, model), value))
        model.add_up_linkages_to_final_result(linkages)
        model.sanity_check()
        model.draw_linkage()

    def __get_linkage_for_component(self, component, model: Model):
        sub_components = component.args[0].as_coefficients_dict().items()
        alpha, beta = sy.symbols('alpha beta')
        alpha_linkage = None
        beta_linkage = None
        add_pi = 0
        for angle, factor in sub_components:
            if angle == alpha:
                alpha_linkage = model.create_and_get_multiplicator_of_factor(factor, "alpha")
            elif angle == beta:
                beta_linkage = model.create_and_get_multiplicator_of_factor(factor, "beta")
            else:
                add_pi = factor
        result_linkage = alpha_linkage if beta_linkage is None else beta_linkage
        result_linkage = model.add_angles(alpha_linkage, beta_linkage) if ((alpha_linkage is not None) and (beta_linkage is not None)) else result_linkage
        return model.add_or_substract_half_pi_to_linkage_angle(result_linkage, True if add_pi > 0 else False) if add_pi != 0 else result_linkage


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
    
