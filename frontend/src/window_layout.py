from argparse import ArgumentError
from zoneinfo import reset_tzpath
import PySimpleGUI as sg

class WindowLayout:

    __methods = {
        "Polynomial of Degree N": {
            "short_name": "POLYNOMIAL",
            "parameters": [
                {"name": "N", "description_text": "n = ", "type": "free", "default": "2"}
            ]
        },
        "Some other test method that is not implemented": {
            "short_name": "FOO",
            "parameters" : [
                {"name": "A", "description_text": "a text field", "type": "free", "default": ""},
                {"name": "B", "description_text": "a selection field", "type": "selection", "values": ["Eins", "Zwei", "Drei"]}
            ]
        }
    }
        
    def get_layout(self):
        return [
            [
                self.__get_parameters_column(),
                sg.VSeperator(),
                sg.Column([
                    [sg.Text("Please select the desired approximation technique.")],
                    [sg.Combo(list(self.__methods.keys()), readonly=True, enable_events=True, key="METHOD_SELECTION")],
                    [sg.Canvas(size = (700, 400), background_color="white")]
                ], size = (800, None))
            ]
        ]

    def __get_parameters_column(self):
        col = []
        for key, method in self.__methods.items():
            method_layout = []
            for param in method["parameters"]:
                row = []
                row.append(sg.Text(param["description_text"]))
                if param["type"] == "free":
                    row.append(sg.Input(default_text=param["default"], key="_".join([method["short_name"], param["name"]])))
                elif param["type"] == "selection":
                    row.append(sg.Combo(param["values"], default_value=param["values"][0], 
                        readonly=True, key="_".join([method["short_name"], param["name"]])))
                else:
                    raise ValueError("This parameter type is unknown")
                method_layout.append(row)

            col.append([sg.Frame(title=key, border_width=0, layout=method_layout, visible=False, key="_".join([method["short_name"], "FRAME"]))])

        return sg.Column(col, size = (400, None))

    def switch_parameter_group(self, window):
        for key, method in self.__methods.items():
            window["_".join([method["short_name"], "FRAME"])].update(visible=False)
        method = self.__methods[window["METHOD_SELECTION"].get()]
        window["_".join([method["short_name"], "FRAME"])].update(visible=True)