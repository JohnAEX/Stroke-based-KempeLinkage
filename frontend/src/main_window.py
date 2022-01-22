import PySimpleGUI as sg
import math
from window_layout import WindowLayout

STROKE_WIDTH = 2
POINT_DISTANCE_THRESHOLD = 20
points = []
def paint(event):
    python_green = "#476042"
    w = window["CANVAS"].tk_canvas
    if len(points) > 0 and math.sqrt((event.x - points[-1][0])**2 + (event.y - points[-1][1])**2) < POINT_DISTANCE_THRESHOLD:
        w.create_line(event.x,event.y,points[-1][0],points[-1][1], fill="blue", width=STROKE_WIDTH)
    points.append([event.x, event.y])
    


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