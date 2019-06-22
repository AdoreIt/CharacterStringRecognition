import cv2

from Graph import *


class Recognizer:
    def __init__(self, image_reference, noised_image, alphabet,
                 characters_dict):
        self.image_reference = image_reference
        self.noised_image = noised_image
        self.im_height = noised_image.shape[0]
        self.characters_dict = characters_dict

        self.graph = Graph(image_reference.shape[1], alphabet, characters_dict)

        #self.graph.print_graph()

    def update_edges(self):
        for column in self.graph.columns:
            for vertice in column.vertices:
                for edge in vertice.edges:
                    #print(column.index)
                    reference_char = self.characters_dict[edge.head.label]
                    edge.weight = self.sum_of_squared_differences(
                        reference_char, column.index)

    def sum_of_squared_differences(self, reference_char,
                                   image_start_column_index):
        """
        """
        # row, col
        char_width = reference_char.shape[1]

        im_col = image_start_column_index
        sum = 0

        for column in range(char_width - 1):
            #print("char_width: {}".format(range(char_width)))

            for pixel in range(0, self.im_height - 1):
                # print("im_height: {}".format(range(im_height)))
                # print("column: {}, pixel: {}".format(column, pixel))
                # print("im_column: {}".format(im_col))
                # print(sum)

                # print(
                #     cv2.ad.sum(
                #         cv2.subtract(
                #             self.noised_image[pixel, image_start_column_index +
                #                               column],
                #             reference_char[pixel, column])))
                sum += (np.sum(
                    cv2.subtract(
                        self.noised_image[pixel, image_start_column_index +
                                          column],
                        reference_char[pixel, column])))**2

        return sum