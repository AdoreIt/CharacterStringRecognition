from matplotlib import pyplot as plt
import numpy as np
import cv2


def draw_letters(letters_string):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.55
    margin = 4
    thickness = 2
    color = (0, 0, 0)

    size = cv2.getTextSize(letters_string, font, font_scale, thickness)

    text_width = size[0][0]
    text_height = size[0][1]

    print(text_width)
    print(text_height)

    image = np.zeros((text_height + margin, text_width + margin, 3), np.uint8)
    image.fill(255)

    textX = int((image.shape[1] - text_width) / 2)
    textY = int((image.shape[0] + text_height) / 2)
    
    cv2.putText(image, letters_string, (textX, textY), font, font_scale, color, thickness)

    return image

def show_image(image):
    plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()
