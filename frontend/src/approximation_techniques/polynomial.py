from approximation_techniques.base_approximation import BaseApproximation
from scipy.optimize import curve_fit as cf
from types import FunctionType

class PolynomialApproximation(BaseApproximation):

    def get_function(self, n):
        func =  f'def approx(x, {", ".join(["a" + str(i) for i in range(n)])}):\n  return {" + ".join(["a" + str(i) + ("*x**") + str(i) for i in range(n)])}'
        f_code = compile(func, "<float>", "exec")
        f_func = FunctionType(f_code.co_consts[0], globals(), "approx")

        return f_func

    def foo(self, x, a):
        return x*a

    def set_parameters_and_approximate(self, parameter_map, xdata, ydata):
        n = int(parameter_map["N"])
        self.__func = self.get_function(n)
        popt, pcov = cf(self.__func, xdata, ydata)
        self.__popt = popt

    def get_approximated_function(self):
        n = len(self.__popt)
        func =  f'def approx(x):\n  return {" + ".join([str(self.__popt[i]) + ("*x**") + str(i) for i in range(n)])}'
        print(func)
        f_code = compile(func, "<float>", "exec")
        f_func = FunctionType(f_code.co_consts[0], globals(), "approx")
        return FunctionType(f_code.co_consts[0], globals(), "get_approx_value")