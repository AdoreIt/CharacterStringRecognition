from Graph import *


class Recognizer:
    def __init__(self, image_reference, noised_image, alphabet,
                 characters_dict):
        self.image_reference = image_reference
        self.noised_image = noised_image
        self.characters_dict = characters_dict

        self.graph = Graph(image_reference.shape[1], alphabet, characters_dict)

        self.graph.print_graph()

    def update_edges(self):
        for column in self.graph.columns:
            for vertice in column.vertices:
                for edge in vertice.edges:
                    #print(column.index)
                    edge.weight = self.sum_of_squared_differences(
                        self.characters_dict[vertice.label].shape[1],
                        column.index)

    def sum_of_squared_differences(self, char_width, image_start_column_index):
        """
        """
        # row, col
        im_height, im_width, channels = self.image_reference.shape
        im_col = image_start_column_index
        sum = 0

        for column in range(image_start_column_index,
                            image_start_column_index + char_width - 1):
            print("char_width: {}".format(range(char_width)))

            for pixel in range(0, im_height - 1):
                print("im_height: {}".format(range(im_height)))
                print("column: {}, pixel: {}".format(column, pixel))
                print("im_column: {}".format(im_col))
                print(sum)

                sum += (np.sum(
                    np.subtract(self.image_reference[pixel:column],
                                self.noised_image[pixel, column])))**2

        return sum