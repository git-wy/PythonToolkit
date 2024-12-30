# -*- coding: utf-8 -*-
# Author: Wendy WANG
# Modified: 12/30/2024

import os

from PIL import Image


def images2pdf(image_input, pdf_output):
    """
    combine all images in a folder and convert them to one pdf file

    :param image_input: a folder saving images to be converted
    :param pdf_output: pdf file path
    :return:
    """
    images = [
        Image.open(os.path.join(image_input, img)).convert("RGB")
        for img in sorted(os.listdir(image_input))
    ]
    if images:
        images[0].save(pdf_output, save_all=True, append_images=images[1:])
        print(f"PDF created: {pdf_output}")
    else:
        print("No images found.")


if __name__ == '__main__':

    my_image_input = r'../image_input_folder/'
    my_pdf_output = r'../my_pdf_output.pdf'

    images2pdf(my_image_input, my_pdf_output)
