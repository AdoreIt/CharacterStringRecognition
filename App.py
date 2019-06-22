from VizGen import *
from Recognizer import Recognizer

if __name__ == "__main__":
    alphabet = ['A']

    generated_string, characters_dict, original_image = generate_image(
        alphabet, 3)
    noised_image = noise_image(original_image, sigma=500)

    recognizer = Recognizer(original_image, noised_image, alphabet,
                            characters_dict)

    recognized_string = recognizer.recognize()
    recognized_image = concatenate_images(recognized_string, characters_dict)

    show_triple_images(original_image, noised_image, recognized_image,
                       "original image", "noised image", "recognized image")

    # show_image(noise_image(image, 0, 20), "noised image")