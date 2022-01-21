import PySimpleGUI as sg
from window_layout import WindowLayout

STROKE_WIDTH = 2
points = []
def paint(event):
    python_green = "#476042"
    w = window["CANVAS"].tk_canvas
    x1, y1 = ( event.x - STROKE_WIDTH ), ( event.y - STROKE_WIDTH )
    x2, y2 = ( event.x + STROKE_WIDTH ), ( event.y + STROKE_WIDTH )
    points.append([event.x, event.y])
    w.create_oval( x1, y1, x2, y2, fill = "blue" )


layout = WindowLayout()

window = sg.Window(title="Kempe Linkage", layout=layout.get_layout(), margins=(10, 10), finalize=True)
window["CANVAS"].tk_canvas.bind("<Button1-Motion>", paint)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "METHOD_SELECTION":
        layout.switch_parameter_group(window)

window.close()
print(points)