import sympy as sy

class function_exporter:

    def __init__(self, function: sy.core.add.Add) -> None:
        self.__function = function
        self.__prepare_function()
    
    def __prepare_function(self) -> None:
        alpha,beta,r,x,y = sy.symbols('a b r x y')
        print(self.__function)
        self.__function = self.__function.subs(r, 1)
        max = 0
        print(self.__function)
        for key, value in self.__function.as_coefficients_dict().items():
            #print(key.args, value)
            if len(key.args)>max:
                max = len(key.args)
                #print(type(key.args[0]))
            #print(dir(key))
        print(max)
        #sy.pprint(self.__function)