import random
import string

from pyslvs import VPoint, VJoint, VLink


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# todo: determine what VLink would want for a 'collections.abc.Sequence[int]' to reverse the initialization
def rhombus_link(points):
    links = []
    link_amount = 4
    counter = 0
    while counter < link_amount:
        links.append(VLink(generate_name("Link", counter), "blue", list()))
        counter += 1
    # todo: how do we dynamically add and remove links ?
    points[0].set_links(['ground', links[0].name, links[3].name])
    points[3].set_links([links[3].name, links[2].name])
    points[1].set_links([links[0].name, links[1].name])
    points[2].set_links([links[1].name, links[2].name])


def counter_parallelogram_link(points):
    links = []
    link_amount = 4
    counter = 0
    while counter < link_amount:
        links.append(VLink(generate_name("Link", counter), "blue", list()))
        counter += 1
    # todo: how do we dynamically add and remove links ?
    points[0].set_links(['ground', links[0].name, links[2].name])
    points[3].set_links([links[3].name, links[1].name])
    points[1].set_links([links[0].name, links[1].name])
    points[2].set_links([links[3].name, links[2].name])


def generate_name(base, counter):
    return base + "_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + "_" + str(counter)


class Rhombus:
    points = []
    links = []

    def __init__(self, p1, p2, p3, p4):
        self.points.extend([point_to_vpoint(p1), point_to_vpoint(p2), point_to_vpoint(p3), point_to_vpoint(p4)])
        rhombus_link(self.points)


class CounterParallelogram:
    points = []

    def __init__(self, p1, p2, p3, p4):
        self.points.extend([point_to_vpoint(p1), point_to_vpoint(p2), point_to_vpoint(p3), point_to_vpoint(p4)])
        counter_parallelogram_link(self.points)


# example: VPoint(('ground', 'L1'), 0, 0.0, [[-67.38, 36.13], [0.0, 0.0]])
def point_to_vpoint(point):
    # todo: differentiate between R / P / RP Joints
    point = VPoint('', VJoint.R, 0, "blue", point.x, point.y)
    print()
    return point


def geometry_to_expression(geo):
    """ Return a valid Mechanism-Expression based on the VPoints in a Geometry object
    that can then be imported into pyslvs """
    expression = "M["
    for p in geo.points:
        expression += "\n" + p.expr() + ","
    expression += "\n]"
    return expression


def geometries_to_expression(geos):
    expression = "M["
    for geo in geos:
        for p in geo.points:
            expression += "\n" + p.expr() + ","
    expression += "\n]"
    return expression
