from VizGen import *
from Recognizer import Recognizer

if __name__ == "__main__":
    alphabet = ['B', 'A', 'D', 'C']  # 'L', 'C']

    generated_string, characters_dict, original_image = generate_image(
        alphabet, 8)
    noised_image = noise_image(original_image, sigma=600)
    #show_image(noised_image)

    recognizer = Recognizer(original_image, noised_image, alphabet,
                            characters_dict)

    print(original_image.shape[1])
    print(noised_image.shape[1])

    recognized_string = recognizer.recognize()
    recognized_image = concatenate_images(recognized_string, characters_dict)

    show_triple_images(original_image, noised_image, recognized_image,
                       "original image", "noised image", "recognized image")

    # show_image(noise_image(image, 0, 20), "noised image")