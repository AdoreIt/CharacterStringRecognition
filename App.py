from VizGen import *

if __name__ == "__main__":
    alphabet = ['A', 'G', 'L', 'B', ' ']

    image = generate_image(alphabet, 5)
    show_image(image, "generated image")

    show_image(noise_image(image, 0, 20), "noised image")