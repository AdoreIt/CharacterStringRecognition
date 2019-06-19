import matplotlib.pyplot as plt
import numpy as np
import cv2


def generate_string(alphabet, length):
    return ''.join(np.random.choice(alphabet, length))


def draw_letters(letters_string):
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    margin = 4
    thickness = 2
    color = (0, 0, 0)

    size = cv2.getTextSize(letters_string, font, font_scale, thickness)

    text_width = size[0][0]
    text_height = size[0][1]

    image = np.zeros((text_height + margin, text_width + margin, 3), np.uint8)
    image.fill(255)

    textX = int((image.shape[1] - text_width - margin / 2) / 2)
    textY = int((image.shape[0] + text_height - margin / 2) / 2)

    cv2.putText(image, letters_string, (textX, textY), font, font_scale, color,
                thickness)

    return image


def generate_image(alphabet, length):
    return draw_letters(generate_string(alphabet, 5))


def noise_image(image, mean=0, sigma=0):
    im_width, im_height, channels = get_im_size(image)

    gaussian = np.random.normal(mean, sigma, (im_height, im_width))

    noisy_image = np.zeros(image.shape, np.float32)

    if len(channels) == 2:
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


def get_im_size(image):
    return (image.shape[1], image.shape[0], image.shape)