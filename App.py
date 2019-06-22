from VizGen import generate_image
from Recognizer import Recognizer

if __name__ == "__main__":
    alphabet = ['A']

    generated_string, characters_dict, image = generate_image(alphabet, 1)

    #show_image(image, "generated image")

    recognizer = Recognizer(image, image, alphabet, characters_dict)
    #recognizer.update_edges()
    #recognizer.graph.print_graph()

    # show_image(noise_image(image, 0, 20), "noised image")