# -*- coding: utf-8 -*-
# Author: Wendy WANG
# Modified: 12/30/2024

import os

from PIL import Image


def resize_image(image_input, image_output, mode='resize',
                 size: tuple[int, int] | None = None,
                 crop_box: tuple[float, float, float, float] | None = None):
    """
    resize or crop all images into the same size in a folder

    :param image_input: a folder saving images to be processed
    :param image_output: a folder saving processed images
    :param mode: string, 'resize' or 'crop'.
        'resize' scales the entire image to change its size without altering the content
        'crop' changes the size by removing parts of the image
    :param size: tuple, (width, height)
    :param crop_box: tuple, (left, top, right, bottom)
    :return:
    """

    os.makedirs(image_output, exist_ok=True)
    for filename in os.listdir(image_input):
        input_path = os.path.join(image_input, filename)
        output_path = os.path.join(image_output, filename)
        with Image.open(input_path) as img:
            if mode == "resize" and size:
                processed_img = img.resize(size, Image.Resampling.LANCZOS)
            elif mode == "crop" and crop_box:
                left, top, right, bottom = crop_box
                processed_img = img.crop((left, top, img.width - right, img.height - bottom))
            else:
                raise ValueError("Invalid mode or missing parameters.")
            processed_img.save(output_path)
    print(f"Processed images saved to {image_output}")


if __name__ == '__main__':

    my_image_input = r'../image_input_folder/'
    my_image_output = r'../image_output_folder/'

    resize_image(my_image_input, my_image_output, mode='resize', size=(1190, 1490))
    resize_image(my_image_input, my_image_output, mode='crop', crop_box=(0, 0, 300, 400))
