from model_export.geometry import Geometry
from model_export.linkage import Linkage
from model_export.node import Node
from model_export.geometry import Geometry
import math

class Model:

    def __init__(self, scale_factor=256, initial_angle=math.pi/4) -> None:
        self.__scale_factor = scale_factor
        self.__inital_angle = initial_angle
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
        length_a = math.sqrt(5*self.__scale_factor**2-4*self.__scale_factor**2*math.cos(self.__inital_angle))
        upper_angle = math.pi - math.asin(math.sin(self.__inital_angle)*2*self.__scale_factor/length_a) 
        x_angle = 1/2 * math.pi - (upper_angle - (math.pi - self.__inital_angle - upper_angle) )
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
        new_x = math.cos(level * self.__inital_angle) * new_length * (1 if angle == "alpha" else -1)
        new_y = math.sin(level * self.__inital_angle) * new_length
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

    def add_angles(self, linkage_a: Linkage, linkage_b: Linkage) -> None:
        short_edge, long_edge = self.__get_short_edge_long_edge(linkage_a, linkage_b)
        reference_node = self.__get_outer_node(long_edge)
        new_node = self.__get_new_node(short_edge, long_edge, reference_node)

    def __get_short_edge_long_edge(self, linkage_a: Linkage, linkage_b: Linkage) -> tuple[Linkage, Linkage]:
        outer_node_a = self.__get_outer_node(linkage_a)
        outer_node_b = self.__get_outer_node(linkage_b)
        angle_a = self.__get_angle_of_node(outer_node_a)
        angle_b = self.__get_angle_of_node(outer_node_b)
        return linkage_a, linkage_b if angle_a > angle_b else linkage_b, linkage_a

    def __get_angle_of_node(self, node: Node) -> float:
        x,y = node.get_xy()
        hypothenuses_length = self.__pythagoras2(x,y)
        base_angle = math.asin(math.abs(y)/hypothenuses_length)
        if x > 0:
            if y > 0:
                return base_angle
            else:
                return 2 * math.pi - base_angle
        else:
            if y > 0:
                return math.pi - base_angle
            else:
                return math.pi + base_angle


    def __get_new_node(self, short_edge, long_edge, reference_node):
        new_node = None
        if long_edge.get_length != short_edge.get_length * 2:
            new_x = reference_node.get_x() * 2 * short_edge.get_length() / long_edge.get_length
            new_y = reference_node.get_y() * 2 * short_edge.get_length() / long_edge.get_length
            new_node = Node(["helper"], False, (new_x, new_y))
            self.__all_geometry.append(new_node)
        else:
            new_node = reference_node
        return new_node

    def __get_outer_node(self, linkage: Linkage) -> Node:
        return linkage_a.get_nodes()[0] if linkage_a.get_nodes()[0] != self.__origin else linkage_a.get_nodes()[1]

# TODO:
# Zwei Winkel addieren
    # Den kleineren Winkel als lange Kante des inneren Counterparallelograms nehmen x
    # Den längeren auf der Hälfte des kürzeren Abtragen (kürzen oder verlängern) x 
    # Unteren Punkt des großen Parallelograms berechnen (der Winkel unten ist die Summe von beiden /2 - der kleinere Winkel)
    # Den Winkel oben muss ich noch überlegen
    # Dann den alpha+beta/2 einzeichnen (einfach, wir kennen ja den Winkel) länge ist die kurze Seite des großen Parallelograms
    # Dann fehlt für das kleinere Parallelogramm nur noch ein Balken. Der ergibt sich wie beim Multiplikator durch 1/4 * Vektor Richtung unten
    # Jetzt muss der Winkel noch verdoppelt werden. Dazu nimmt man die Addition als kurze Seite des großen und lange Seite des kleinen PaLeG
    # Wo das Ergebnis liegt wissen wir -> Winkel mal 2, Länge/2
    # Die untere Kante des großen PLG liegt auf der Horizontalen und ist fix
    # Für den unteren Punkt die Formel nutzen, die schon für den Multiplikator notwendig war
    # Jetzt fertig machen -> Eigentlich ist das ja nur ein Multiplikator -> Da sollte sich die Funktion nochmal verwenden lassen
# pi/2 auf einen Winkel addieren
# Ergebnisse entsprechend Faktor verlängern
# Ergebnisse durch Translatoren verbinden

    def get_geometry(self):
        return self.__all_geometry
