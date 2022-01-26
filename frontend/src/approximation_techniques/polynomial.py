from approximation_techniques.base_approximation import BaseApproximation

class PolynomialApproximation(BaseApproximation):
    def set_parameters_and_approximate(self, parameter_map, xdata, ydata):
        n = int(parameter_map["N"])
        function = f'''def polynomial_approximation(x, {", ".join(["a" + str(i) for i in range(n)])}):
            \treturn {" + ".join(["a" + str(i) + ("*x**") + str(i) for i in range(n)])}'''

        print(function)

    def get_approximated_function(self):
        pass