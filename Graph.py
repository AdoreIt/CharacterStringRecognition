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
            tail_column_index = column.index + c_w_d[char] - 1

            if (tail_column_index < len(self.columns)):
                edge = Edge({column.index: vertice.label},
                            head={tail_column_index: char})
                vertice.add_edge(edge)

    def print_graph(self):
        for i, column in enumerate(self.columns):
            column.print_column(i)


class Column:
    def __init__(self, vertices, column_index=0):
        self.vertices = vertices
        self.index = column_index

    def print_column(self, index=None):

        print("┌──── COLUMN {} ───┐".format(index))
        for vertice in self.vertices:
            vertice.print_vertice()
        print("└──────────────────┘")


class Vertice:
    def __init__(self, label=None, edges=[], weight=0, previous=None):
        self.label = label
        self.weight = weight
        self.previous = previous
        self.edges = list(edges)

    def add_edge(self, edge):
        self.edges.append(edge)

    def update(self, weight, previous=None):
        self.weight = weight
        self.previous = previous

    def print_vertice(self):
        print("│ ┌───── {} ──────┐ │".format(self.label))
        print("│ │w: {0}".format(self.weight) +
              str("|").rjust(12 - len(str(self.weight))) + " |")
        #print("│ w│ {:>11}".format(self.weight, "|"))
        print("│ ├──────────────┤ │")

        for edge in self.edges:
            edge.print_edge()

        print("│ └──────────────┘ │")


class Edge:
    def __init__(self, tail=None, head=None, weight=np.inf):
        """ 
        - tail: vertice.label, column.index
        """
        self.weight = weight
        self.tail = tail
        self.head = head

    def print_edge(self):
        print("│ ├──> {0} : {1}".format(self.head, self.weight) +
              str("|").rjust(7 - len(str(self.weight))) + " |")
