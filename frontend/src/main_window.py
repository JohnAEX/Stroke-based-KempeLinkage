import PySimpleGUI as sg
from window_layout import WindowLayout

layout = WindowLayout()

sg.Window(title="Kempe Linkage", layout=layout.get_layout(), margins=(100, 50)).read()

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()