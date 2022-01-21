from zoneinfo import reset_tzpath
import PySimpleGUI as sg

class WindowLayout:

    def __init__(self) -> None:
        self.layout = []

    def get_layout(self):
        self.layout.extend(self.__get_menu())

        return self.layout
        
    def __get_menu(self):
        return [
            [sg.Text("Please select the desired approximation technique.")],
            [sg.Combo(["polynomial"], default_value="polynomial", readonly=True)]
        ]