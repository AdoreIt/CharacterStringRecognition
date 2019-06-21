import numpy as np


class Graph:
    def __init__(self, columns_number, alphabet, vertices=[], edges=[]):
        """ 
        - columns_number: image.width
        """
        self.vertices = [
            Vertice(label=label,
                    edges=[
                        Edge(tail=label, head=character)
                        for character in alphabet
                    ]) for label in alphabet
        ]
        self.columns = [Column(self.vertices) for _ in range(columns_number)]
        self.edges = edges
        self.initialize()

    def initialize(self):
        """ Initialization """

    def add_column(self):
        """ Adding column """

    def print_graph(self):
        for i, column in enumerate(self.columns):
            column.print_column(i)


class Column:
    def __init__(self, vertices):
        self.vertices = vertices

    def print_column(self, index=None):

        print("┌──── COLUMN {} ────┐".format(index))
        for vertice in self.vertices:
            vertice.print_vertice()
        print("└──────────────────┘")


class Vertice:
    def __init__(self, label=None, edges=[], weight=0, previous=None):
        self.label = label
        self.weight = weight
        self.previous = previous
        self.edges = edges

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
