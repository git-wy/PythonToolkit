# -*- coding: utf-8 -*-
# Author: Ying Wang

import cv2


def convert_signature(input_photo, output_name):

    img = cv2.imread(input_photo, cv2.IMREAD_UNCHANGED)
    size = img.shape

    for i in range(size[0]):
        for j in range(size[1]):
            if img[i][j][0] > 80 and img[i][j][1] > 80 and img[i][j][2] > 80:
                img[i][j][3] = 0
            else:
                img[i][j][0], img[i][j][1], img[i][j][2] = 0, 0, 0

    cv2.imwrite(output_name, img)
    print("Successfully converted into digital signature!")


if __name__ == '__main__':

    photo = r'DigitalSignature/data/InputPhoto.png'
    signature = r'DigitalSignature/data/OutputSignature.png'

    convert_signature(photo, signature)

