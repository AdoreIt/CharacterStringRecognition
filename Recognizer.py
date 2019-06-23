import cv2

from Graph import *


class Recognizer:
    def __init__(self, image_reference, noised_image, alphabet,
                 characters_dict):
        self.image_reference = image_reference
        self.noised_image = noised_image
        self.im_width = noised_image.shape[1]
        self.im_height = noised_image.shape[0]
        self.characters_dict = characters_dict

        print(self.im_width)

        self.graph = Graph(image_reference.shape[1], alphabet, characters_dict)

        #self.graph.print_graph()

    def recognize(self):
        self.update_edges()
        self.graph.print_graph()
        self.answer()
        self.graph.print_graph()
        return self.print_recognized_string()

    def print_recognized_string(self):
        recognized_string = ""
        current_best_edge = self.graph.columns[0].vertices[0].best_edge
        recognized_string += current_best_edge.head.label
        #print(current_best_edge.head.label)

        while current_best_edge is not None:
            # print(current_best_edge.tail.column_index)
            # print(current_best_edge.head.column_index)
            current_best_edge = self.get_next_best_edge(current_best_edge.head)
            if (current_best_edge is not None):
                #print(current_best_edge.head.label)
                recognized_string += current_best_edge.head.label

        print("Recognized string: '{}'".format(recognized_string))
        # best_column = self.graph.columns[best_edge_head.column_index]
        # best_vertice_in_column = best_column.get_vertice_by_label[
        #     best_edge_head.label]
        return recognized_string

    def get_next_best_edge(self, current_best_edge_head):
        if len(self.graph.columns) > current_best_edge_head.column_index + 1:
            best_column = self.graph.columns[current_best_edge_head.column_index
                                             + 1]
            best_vertice_in_column = best_column.get_vertice_by_label(
                current_best_edge_head.label)
            next_best_edge = best_vertice_in_column.best_edge
            return next_best_edge

    def answer(self):
        columns = self.graph.columns
        for column_index in reversed(range(1, len(self.graph.columns) + 1)):
            for vertice in columns[column_index - 1].vertices:
                edges_head_vertices_sum = {}  # {edge.head.label: sum}

                if len(vertice.edges) != 0:
                    print("{} {}: ".format(column_index - 1, vertice.label))

                    for edge in vertice.edges:
                        edge_head_column = columns[edge.head.column_index]
                        edge_head_vertice_weight = edge_head_column.get_vertice_by_label(
                            edge.head.label).weight

                        print("{} {} ----{}----> {} {} {}".format(
                            edge.tail.column_index, edge.tail.label,
                            edge.weight, edge_head_column.index,
                            edge.head.label, edge_head_vertice_weight))
                        # print('edge_head_column {}'.format(
                        #     edge_head_column.index))
                        # print('edge.head.label {}'.format(edge.head.label))
                        # print('edge_head_vertice_weight {}'.format(
                        #     edge_head_vertice_weight))

                        edge_head_vertice_sum = edge_head_vertice_weight + edge.weight
                        edges_head_vertices_sum[
                            edge.head.label] = edge_head_vertice_sum

                    print(edges_head_vertices_sum)

                    min_head_vertice_label = min(
                        edges_head_vertices_sum,
                        key=edges_head_vertices_sum.get)
                    min_head_vertice_sum = edges_head_vertices_sum[
                        min_head_vertice_label]

                    vertice.weight += min_head_vertice_sum
                    vertice.best_edge = vertice.get_edge_by_head_label(
                        min_head_vertice_label)

                    best_edge_head_column = columns[
                        vertice.best_edge.head.column_index]
                    best_edge_head_vertice_weight = edge_head_column.get_vertice_by_label(
                        vertice.best_edge.head.label).weight

                    print("best_edge: {} {} ----{}----> {} {} {}".format(
                        vertice.best_edge.tail.column_index,
                        vertice.best_edge.tail.label, vertice.best_edge.weight,
                        best_edge_head_column.index,
                        vertice.best_edge.head.label,
                        best_edge_head_vertice_weight))

                    print("\n\n --------- \n\n")
                    print("\n\n --------- \n\n")

    def update_edges(self):
        for column in self.graph.columns:
            for vertice in column.vertices:
                for edge in vertice.edges:
                    #print(column.index)
                    reference_char = self.characters_dict[edge.head.label]
                    #print(edge.head.label)
                    edge.weight = self.sum_of_squared_differences(
                        reference_char, column.index)

    def sum_of_squared_differences(self, reference_char,
                                   image_start_column_index):
        char_width = reference_char.shape[1]
        #print(char_width)

        im_col = image_start_column_index
        sum = 0

        for column in range(char_width):
            #print("char_width: {}".format(range(char_width)))

            for pixel in range(self.im_height):
                # print("im_height: {}".format(range(im_height)))
                # print("column: {}, pixel: {}".format(column, pixel))
                # print("im_column: {}".format(im_col))
                # print(sum)

                sum += (np.sum(
                    cv2.absdiff(
                        self.noised_image[pixel, image_start_column_index +
                                          column - 1],
                        reference_char[pixel, column - 1])))**2

        return sum