from zoneinfo import reset_tzpath
import PySimpleGUI as sg

class WindowLayout:

    __methods = {
        "polynomial of degree n": {}
    }

    def __init__(self) -> None:
        self.layout = []

    def get_layout(self):
        self.layout.extend(self.__get_layout())

        return self.layout
        
    def __get_layout(self):
        return [
            [
                self.__get_parameters_column(),
                sg.VSeperator(),
                sg.Column([
                    [sg.Text("Please select the desired approximation technique.")],
                    [sg.Combo(list(self.__methods.keys()), default_value=list(self.__methods.keys())[0], readonly=True, enable_events=True, key="METHOD_SELECTION")]
                ], size = (500, None))
            ]
        ]

    def __get_parameters_column(self):
        return sg.Column([
            [sg.Text("n = "), sg.Input(default_text="2", key="POLYNOMIAL_N")]
        ], size = (200, None))