from pyslvs import VPoint, VJoint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# todo: determine in what order points should be defined (BFS vs. DFS)
class Rhombus:
    points = []

    def __init__(self, p1, p2, p3, p4):
        self.points.extend([point_to_vpoint(p1), point_to_vpoint(p2), point_to_vpoint(p3), point_to_vpoint(p4)])


# linkage will be different from Rhombus, linkage not implemented yet
class CounterParallelogram:
    points = []

    def __init__(self, p1, p2, p3, p4):
        self.points.extend([point_to_vpoint(p1), point_to_vpoint(p2), point_to_vpoint(p3), point_to_vpoint(p4)])


# example: VPoint(('ground', 'L1'), 0, 0.0, [[-67.38, 36.13], [0.0, 0.0]])
def point_to_vpoint(point):
    # todo: implement linkage
    # todo: differentiate between R / P / RP Joints
    return VPoint('', VJoint.R, 0, "blue", point.x, point.y)


def geometry_to_expressions(geo):
    """ Return a valid Mechanism-Expression based on the VPoints in a Geometry object
    that can then be imported into pyslvs """
    expression = "M["
    for p in geo.points:
        expression += "\n" + p.expr() + ","
    expression += "\n]"
    return expression
