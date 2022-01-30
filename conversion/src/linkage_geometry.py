import random
import string

from pyslvs import VPoint, VJoint, VLink
from conversion.src.utils import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rhombus:
    # stores points as [{'name': name, 'vpoint': vpoint, 'role': [roles]}]
    points = []
    # stors vlinks as [vlinks]
    links = []

    def __init__(self, o, b, a, d):
        self.points.extend([
            vpoint_to_detailed_point(generate_name("Point", 0), point_to_vpoint(o, "GREEN"),
                                     [Role.INPUT_ALPHA, Role.INPUT_BETA]),
            vpoint_to_detailed_point(generate_name("Point", 1), point_to_vpoint(b), [Role.INPUT_BETA]),
            vpoint_to_detailed_point(generate_name("Point", 2), point_to_vpoint(a), [Role.INPUT_ALPHA]),
            vpoint_to_detailed_point(generate_name("Point", 3), point_to_vpoint(d, "RED"), [Role.OUTPUT])
        ])
        self.links.extend(rhombus_link(self.points))


# todo: fix input roles for usage in multiplicator & additor
class CounterParallelogram:
    # stores points as [{'name': name, 'vpoint': vpoint, 'role': [roles]}]
    points = []
    # stors vlinks as [vlinks]
    links = []

    def __init__(self, o, i, p, b):
        # for some reason python requires this clearing of self data even though it should belong to the instance anyway
        self.points = []
        self.links = []
        self.points.extend([
            vpoint_to_detailed_point(generate_name("Point", 0), point_to_vpoint(o), [Role.INPUT]),
            vpoint_to_detailed_point(generate_name("Point", 1), point_to_vpoint(i), [Role.INPUT]),
            vpoint_to_detailed_point(generate_name("Point", 2), point_to_vpoint(p), [Role.OUTPUT]),
            vpoint_to_detailed_point(generate_name("Point", 3), point_to_vpoint(b), [Role.OUTPUT])
        ])
        self.links.extend(counter_parallelogram_link(self.points))


class Multiplicator:
    geos = []

    def __init__(self, p1, p2, p3, p4, p5, p6):
        self.geos = []
        cp1 = CounterParallelogram(p1, p2, p3, p4)
        self.geos.append(cp1)
        cp2 = CounterParallelogram(p1, p5, p2, p6)
        self.geos.append(cp2)
        combine_link(self.geos[0].points[1], self.geos[1].points[3], self.geos[0].points[3])


class Additor:
    geos = []

    def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
        self.geos = []
        multi1 = Multiplicator(p1, p2, p3, p4, p5, p6)
        self.geos.append(multi1)
        multi2 = Multiplicator(p1, p7, p8, p9, p10, p11)
        self.geos.append(multi2)
        combine_link(self.geos[0].geos[0].points[0], self.geos[0].geos[0].points[2], self.geos[1].geos[0].points[2])

