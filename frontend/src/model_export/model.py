from model_export.geometry import Geometry
from model_export.linkage import Linkage
from model_export.node import Node
from model_export.geometry import Geometry
import math


class Model:

    def __init__(self, scale_factor=256) -> None:
        self.__scale_factor = scale_factor
        self.__all_geometry: list(Geometry) = []
        self.__maximum_multiplicator= {"alpha": 1, "beta": 1}
        a, b, c, d = self.__make_rhombus_nodes()
        self.__make_rhombus_linkages(a,b,c,d)
        self.__add_initial_counterparallelograms()
             


    def __pythagoras2(self, a: float, b: float) -> float:
        return math.sqrt(a**2 + b**2)

    def __pythagoras(self, c: float) -> float:
        return math.sqrt(c**2 / 2)

    def __make_rhombus_nodes(self):
        a = Node(["rhombus", "origin"], True, (0,0))
        b = Node(["rhombus", "alpha", "1"], False, (self.__pythagoras(self.__scale_factor), self.__pythagoras(self.__scale_factor)))
        c = Node(["rhombus", "beta", "1"], False, (-self.__pythagoras(self.__scale_factor), self.__pythagoras(self.__scale_factor)))
        d = Node(["rhombus", "result"], False, (0, 2*self.__pythagoras(self.__scale_factor)))
        self.__all_geometry.extend([a,b,c,d])
        self.__origin = a
        self.__alpha_node = b
        self.__beta_node = c
        return a,b,c,d

    def __calculate_position_of_lower_point(self) -> tuple[float, float]:
        # I bet, this could be simplified tremendously
        length_a = math.sqrt(5*self.__scale_factor**2-4*self.__scale_factor**2*math.cos(1/4 * math.pi))
        upper_angle = math.pi - math.asin(math.sin(1/4*math.pi)*2*self.__scale_factor/length_a) 
        x_angle = 1/2 * math.pi - (upper_angle - (math.pi - 1/4 * math.pi - upper_angle) )
        y_angle = 1/2 * math.pi - x_angle
        return self.__scale_factor * math.sin(x_angle), self.__scale_factor * math.sin(y_angle)

    def __make_rhombus_linkages(self, a: Node, b: Node, c: Node, d: Node) -> None:
        self.__all_geometry.append(Linkage(["rhombus", "alpha", "1", "short"], a, b, self.__scale_factor))
        self.__all_geometry.append(Linkage(["rhombus", "beta", "1", "short"], a, c, self.__scale_factor))
        self.__all_geometry.append(Linkage(["rhombus"], b, d, self.__scale_factor))
        self.__all_geometry.append(Linkage(["rhombus"], c, d, self.__scale_factor))

    def __add_initial_counterparallelograms(self):
        x,y = self.__calculate_position_of_lower_point()
        for (angle, x_factor, rhombus_node) in [("alpha", 1, self.__alpha_node), ("beta", -1, self.__beta_node)]:
            outer = Node([angle], True, (2 * self.__scale_factor * x_factor, 0))
            lower = Node([angle], False, ((2 * self.__scale_factor - x) * x_factor, -y))
            self.__all_geometry.append(Linkage([angle], self.__origin, outer, self.__scale_factor*2, True))
            self.__all_geometry.append(Linkage([angle, "1", "long"], rhombus_node, lower, self.__scale_factor*2))
            self.__all_geometry.append(Linkage([angle], outer, lower, self.__scale_factor))
            self.__all_geometry.extend([outer, lower])

    def create_multiplicator_of_factor(self, factor: int, angle: str):
        for i in range(self.__maximum_multiplicator[angle] + 1, factor + 1):
            self.__append_multiplicator(i, angle)

        self.__maximum_multiplicator[angle] = factor

    def __append_multiplicator(self, level: int, angle: str):
        new_length = self.__scale_factor/2**(level-1)
        short, long = self.__get_short_and_long_linkage_of_previous_mulitplicator(level, angle)
        handle_node = short.get_nodes()[0] if short.get_nodes()[0] in long.get_nodes() else short.get_nodes()[1]
        distant_node = long.get_nodes()[0] if long.get_nodes()[1] == handle_node else long.get_nodes()[1]
        helper_x = handle_node.get_x() + (distant_node.get_x() - handle_node.get_x()) / 4
        helper_y = handle_node.get_y() + (distant_node.get_y() - handle_node.get_y()) / 4
        helper_node = Node([angle], False, (helper_x, helper_y))
        self.__all_geometry.append(helper_node)
        self.__all_geometry.append(Linkage([angle, str(level-1), "helper"], handle_node, helper_node, new_length))
        self.__all_geometry.append(Linkage([angle, str(level-1), "helper"], helper_node, distant_node, new_length * 3))
        new_x = math.cos(level * math.pi/4) * new_length * (1 if angle == "alpha" else -1)
        new_y = math.sin(level * math.pi/4) * new_length
        new_node = Node([angle, str(level)], False, (new_x, new_y))
        self.__all_geometry.append(new_node)
        self.__all_geometry.append(Linkage([angle, str(level), "short"], self.__origin, new_node, new_length))
        self.__all_geometry.append(Linkage([angle, str(level), "long"], new_node, helper_node, 2 * new_length))

    def __get_short_and_long_linkage_of_previous_mulitplicator(self, level, angle) -> tuple[Linkage, Linkage]:
        short = None
        long = None
        for geom in self.__all_geometry:
            if geom.has_tag(angle) and geom.has_tag(str(level-1)):
                if geom.has_tag("short"):
                    short = geom
                if geom.has_tag("long"):
                    long = geom
        return short, long

    def sanity_check(self, threshold = 1) -> bool:
        for geom in self.__all_geometry:
            if geom.has_tag("linkage"):
                dist = self.__pythagoras2(geom.get_nodes()[0].get_x()-geom.get_nodes()[1].get_x(), geom.get_nodes()[0].get_y()-geom.get_nodes()[1].get_y())
                if abs(dist - geom.get_length()) > threshold and geom.get_nodes()[0] in self.__all_geometry and geom.get_nodes()[1] in self.__all_geometry:
                    print("The model is inconsistant")
                    return False
        print("The model is consistant")
        return True
