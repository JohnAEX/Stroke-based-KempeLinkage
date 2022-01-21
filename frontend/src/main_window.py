import PySimpleGUI as sg
from window_layout import WindowLayout

layout = WindowLayout()

window = sg.Window(title="Kempe Linkage", layout=layout.get_layout(), margins=(10, 10))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "METHOD_SELECTION":
        layout.switch_parameter_group(window)

window.close()