import PySimpleGUI as sg
from window_layout import WindowLayout

layout = WindowLayout().get_layout()

window = sg.Window(title="Kempe Linkage", layout=layout, margins=(20, 20))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    print(event)

window.close()