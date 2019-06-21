from VizGen import *
from Graph import *

if __name__ == "__main__":
    alphabet = ['A', 'B']

    graph = Graph(2, alphabet)
    graph.print_graph()
    # generated_string, characters_dict, image = generate_image(alphabet, 5)
    # show_image(image, "generated image")

    # show_image(noise_image(image, 0, 20), "noised image")