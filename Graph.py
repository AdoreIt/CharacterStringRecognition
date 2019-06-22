import numpy as np
from VizGen import get_characters_width_dict


class Graph:
    def __init__(self,
                 columns_number,
                 alphabet,
                 characters_dict,
                 columns=[],
                 vertices=[],
                 edges=[]):
        """
        - columns_number: image.width
        """
        self.columns = columns
        # self.edges = edges
        self.initialize_columns(alphabet, columns_number)
        self.initialize(characters_dict)

    def initialize_columns(self, alphabet, columns_number):
        column = Column(vertices=[Vertice(label="start")], column_index=0)
        self.columns.append(column)
        for i in range(1, columns_number):
            self.columns.append(
                Column([Vertice(label=character) for character in alphabet],
                       column_index=i))

    def initialize(self, characters_dict):
        characters_width_dict = get_characters_width_dict(characters_dict)
        c_w_d = characters_width_dict

        for column in self.columns:
            for vertice in column.vertices:
                self.add_edges_to_vertice_in_column(column, vertice,
                                                    characters_width_dict)

    def add_edges_to_vertice_in_column(self, column, vertice,
                                       characters_width_dict):
        c_w_d = characters_width_dict

        for char in c_w_d:
            head_column_index = column.index + c_w_d[char] - 1

            if (head_column_index < len(self.columns)):
                tail = EdgeTailHead(vertice.label, column.index)
                head = EdgeTailHead(char, head_column_index)

                edge = Edge(tail=tail, head=head)
                vertice.add_edge(edge)

    def print_graph(self):
        for i, column in enumerate(self.columns):
            column.print_column(i)


class Column:
    def __init__(self, vertices, column_index=0):
        self.vertices = vertices
        self.index = column_index

    def get_vertice_by_label(self, vertice_label):
        for vertice in self.vertices:
            if (vertice.label == vertice_label):
                return vertice

    def print_column(self, index=None):
        print("┌─────── COLUMN {} ──────┐".format(index))
        for vertice in self.vertices:
            vertice.print_vertice()
        print("└────────────────────────┘")


class Vertice:
    def __init__(self, label=None, edges=[], weight=0, best_edge=None):
        self.label = label
        self.weight = weight
        self.best_edge = best_edge
        self.edges = list(edges)

    def get_edge_by_head_label(self, edge_head_label):
        for edge in self.edges:
            if edge.head.label == edge_head_label:
                return edge

    def add_edge(self, edge):
        self.edges.append(edge)

    def update(self, weight, best_edge=None):
        self.weight = weight
        self.best_edge = best_edge

    def print_vertice(self):
        if (self.label == "start"):
            print("│ ┌────── {} ───────┐ │".format(self.label))
        else:
            print("│ ┌──────── {} ─────────┐ │".format(self.label))

        print("│ │w: {0}".format(self.weight) +
              str("|").rjust(18 - len(str(self.weight))) + " |")
        if (self.best_edge is not None):
            print("│ │best_edge: {0} in {1}".format(
                self.best_edge.head.label, self.best_edge.head.column_index) +
                  str("|").rjust(8 -
                                 len(str(self.best_edge.head.column_index))) +
                  " |")
        #print("│ w│ {:>11}".format(self.weight, "|"))
        print("│ ├────────────────────┤ │")

        for edge in self.edges:
            edge.print_edge()

        print("│ └────────────────────┘ │")


class Edge:
    def __init__(self, tail=None, head=None, weight=np.inf):
        """ 
        - tail: vertice.label, column.index
        """
        self.weight = weight
        self.tail = tail
        self.head = head

    def print_edge(self):
        print("│ ├──> {0} in {1} : {2}".format(
            self.head.label, self.head.column_index, self.weight) +
              str("|").rjust(7 - len(str(self.weight))) + " |")


class EdgeTailHead:
    def __init__(self, label, column_index):
        self.label = label
        self.column_index = column_index