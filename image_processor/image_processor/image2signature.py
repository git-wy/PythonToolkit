# -*- coding: utf-8 -*-
# Author: Wendy WANG
# Modified: 12/30/2024

import cv2


def image2signature(image_input, signature_output):
    """
    convert a handwriting image into a clear digital signature by making light pixels transparent and turning dark pixels black

    :param image_input: path saving the handwriting image
    :param signature_output: path saving the digital signature
    :return: a clear digital signature image saved in signature_output
    """

    img = cv2.imread(image_input, cv2.IMREAD_UNCHANGED)

    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    size = img.shape

    for i in range(size[0]):
        for j in range(size[1]):
            if img[i][j][0] > 80 and img[i][j][1] > 80 and img[i][j][2] > 80:
                img[i][j][3] = 0
            else:
                img[i][j][0], img[i][j][1], img[i][j][2] = 0, 0, 0

    cv2.imwrite(signature_output, img)
    print("Successfully converted into digital signature!")


if __name__ == '__main__':

    my_image = r'../img_to_signature.png'
    my_signature = r'../my_signature_output.png'

    image2signature(my_image, my_signature)
