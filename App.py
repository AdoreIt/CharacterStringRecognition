from VizGen import generate_image, show_image, noise_image
from Recognizer import Recognizer

if __name__ == "__main__":
    alphabet = ['A', 'B']

    generated_string, characters_dict, image = generate_image(alphabet, 2)

    show_image(image, "generated image")

    noised_image = noise_image(image, sigma=100)
    show_image(noised_image, "noised image")

    recognizer = Recognizer(image, noised_image, alphabet, characters_dict)
    recognizer.update_edges()
    recognizer.graph.print_graph()

    # show_image(noise_image(image, 0, 20), "noised image")