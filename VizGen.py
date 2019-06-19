import matplotlib.pyplot as plt
import numpy as np
import cv2


def generate_string(alphabet, length):
    return ''.join(np.random.choice(alphabet, length))


def draw_letters(letters_string):
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    margin = 1
    thickness = 2
    color = (0, 0, 0)

    letter_imgs = {}

    for letter in letters_string:
        if letter not in letter_imgs:
            #print(letter)
            size = cv2.getTextSize(letter, font, font_scale, thickness)

            text_width = size[0][0]
            text_height = size[0][1]

            char_img = np.zeros((text_height + margin, text_width + margin, 3),
                                np.uint8)
            char_img.fill(255)

            #print("shape {0}:{1}".format(char_img.shape[1], char_img.shape[0]))

            textY = text_height
            textX = 0

            cv2.putText(char_img, letter, (textX, textY), font, font_scale,
                        color, thickness)

            show_image(char_img)
            letter_imgs[letter] = char_img

    return letter_imgs


def concatenate_images(letters_string, images_dict):
    images = [images_dict[letter] for letter in letters_string]

    height = max(image.shape[0] for image in images)
    width = sum(image.shape[1] for image in images)

    concatenated_image = np.zeros((height, width, 3), np.uint8)

    w_offset = 0
    for image in images:
        h, w, c = image.shape
        concatenated_image[0:h, w_offset:w_offset + w] = image
        w_offset += w

    return concatenated_image


def generate_image(alphabet, length):
    generated_string = generate_string(alphabet, 5)
    #print(generated_string)
    letters_dict = draw_letters(generated_string)
    image = concatenate_images(generated_string, letters_dict)
    return generated_string, letters_dict, image


def noise_image(image, mean=0, sigma=0):
    im_height, im_width, channels = image.shape

    gaussian = np.random.normal(mean, sigma, (im_height, im_width))

    noisy_image = np.zeros(image.shape, np.float32)

    if channels == 2:
        noisy_image = image + gaussian
    else:
        noisy_image[:, :, 0] = image[:, :, 0] + gaussian
        noisy_image[:, :, 1] = image[:, :, 1] + gaussian
        noisy_image[:, :, 2] = image[:, :, 2] + gaussian

    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image


def show_image(image, window_name=""):
    fig = plt.figure(0)
    fig.canvas.set_window_title(window_name)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
    plt.close()