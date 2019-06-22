import numpy as np
from VizGen import get_characters_width_dict


class Graph:
    def __init__(self,
                 columns_number,
                 alphabet,
                 characters_dict,
                 vertices=[],
                 edges=[]):
        """ 
        - columns_number: image.width
        """
        # self.columns.append(Column(vertices=[Vertice(label="start",
        #                             edges=[
        #                                 Edge(tail="start", head=character)
        #                                 for character in alphabet
        #                             ])]))
        self.columns = [
            Column([Vertice(label=label) for label in alphabet], i)
            for i in range(columns_number)
        ]
        self.edges = edges
        self.initialize(characters_dict)

    def initialize(self, characters_dict):
        characters_width_dict = get_characters_width_dict(characters_dict)
        c_w_d = characters_width_dict

        for column in self.columns:
            tail_column_index = 0
            for vertice in column.vertices:
                print(vertice)
                for char in c_w_d:
                    print(char)
                    print(vertice)
                    tail_column_index = column.index + c_w_d[char] - 1
                    print(tail_column_index)
                    print(len(self.columns))
                    print(tail_column_index < len(self.columns))
                    if (tail_column_index < len(self.columns)):
                        edge = Edge({column.index: vertice.label},
                                    head={tail_column_index: char})
                        print("if: ", vertice)
                        vertice.add_edge(edge)

            self.print_graph()

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
        self.edges = edges

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
