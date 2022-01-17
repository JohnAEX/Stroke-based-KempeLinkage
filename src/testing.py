from utils import *

# this generated a valid Mechanism-Expression that can be imported into PYSLVS through "Mechanism -> PASTE"
if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(-1, 1)
    p3 = Point(0, 2)
    p4 = Point(1, 1)
    base = Rhombus(p1, p2, p3, p4)
    print(geometry_to_expression(base))

    cpara = CounterParallelogram(p1, p2, p3, p4)
    print(geometry_to_expression(cpara))

    print("Combined:")
    print(geometries_to_expression((base, cpara)))



