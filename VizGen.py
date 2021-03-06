import matplotlib.pyplot as plt
import numpy as np
import cv2


def generate_string(alphabet, length):
    return ''.join(np.random.choice(alphabet, length))


def draw_characters(alphabet):
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    thickness = 2
    color = (0, 0, 0)

    character_imgs = {}

    for character in alphabet:
        if character not in character_imgs:
            size = cv2.getTextSize(character, font, font_scale, thickness)

            text_width = size[0][0]
            text_height = size[0][1]

            char_img = np.zeros((text_height, text_width, 3), np.uint8)
            char_img.fill(255)

            textY = text_height
            textX = 0

            cv2.putText(char_img, character, (textX, textY), font, font_scale,
                        color, thickness)

            crop_img = char_img[0:text_height, 2:text_width - 3]

            character_imgs[character] = crop_img

    return character_imgs


def get_characters_width_dict(characters_dict):
    characters_width_dict = {}

    for character in characters_dict:
        characters_width_dict[character] = characters_dict[character].shape[1]

    return characters_width_dict


def concatenate_images(characters_string, images_dict):
    images = [images_dict[character] for character in characters_string]

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
    generated_string = generate_string(alphabet, length)
    #print(generated_string)
    characters_dict = draw_characters(alphabet)

    image = concatenate_images(generated_string, characters_dict)
    return generated_string, characters_dict, image


def noise_image(image, mean=0, sigma=0):
    im_height, im_width, channels = image.shape

    gaussian = np.random.normal(mean, sigma, (im_height, im_width))

    noisy_image = np.ones(image.shape, np.float32)

    if channels == 2:
        noisy_image = image + gaussian
    else:
        noisy_image[:, :, 0] = image[:, :, 0] + gaussian
        noisy_image[:, :, 1] = image[:, :, 1] + gaussian
        noisy_image[:, :, 2] = image[:, :, 2] + gaussian

    cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image


def show_triple_images(image_left,
                       image_right,
                       image_low,
                       im_left_title="",
                       im_right_title="",
                       im_low_title="",
                       window_name=""):

    fig = plt.figure(0)

    fig.add_subplot(1, 2, 1)
    plt.title(im_left_title)
    plt.imshow(cv2.cvtColor(image_left, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    fig.add_subplot(1, 2, 2)
    plt.title(im_right_title)
    plt.imshow(cv2.cvtColor(image_right, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    fig.add_subplot(4, 1, 4)
    plt.title(im_low_title)
    plt.imshow(cv2.cvtColor(image_low, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.show()


def show_pair_images(image_left,
                     image_right,
                     im_left_title="",
                     im_right_title="",
                     window_name=""):
    fig = plt.figure(0)

    fig.add_subplot(1, 2, 1)
    plt.title(im_left_title)
    plt.imshow(cv2.cvtColor(image_left, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    fig.add_subplot(1, 2, 2)
    plt.title(im_right_title)
    plt.imshow(cv2.cvtColor(image_right, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.show()


def show_image(image, window_name=""):
    fig = plt.figure(0)
    fig.canvas.set_window_title(window_name)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis("off")

    plt.show()
    plt.close()