# -*- coding: utf-8 -*-
# Author: Ying Wang

from PIL import Image
import os


def image_crop(input_dir, output_dir, box_left, box_up, box_right, box_down):
    """
    crop all images in a directory

    :param input_dir: directory saving images
    :param output_dir: directory saving images after cropping
    :param box_left: the left pixel
    :param box_up: the upper pixel
    :param box_right: the right pixel
    :param box_down: the lower pixel
    :return: cropped images saved in output_dir
    """

    for image_file in os.listdir(input_dir):

        image_input_fullname = input_dir + '/' + image_file
        img = Image.open(image_input_fullname)
        box = (box_left, box_up, box_left + box_right, box_up + box_down)
        image_cropped = img.crop(box)
        image_output_fullname = output_dir + '/' + image_file
        image_cropped.save(image_output_fullname)

        print('Successfully cropped {}.'.format(image_file))


if __name__ == '__main__':

    image_input = r'path saving images'
    image_output = r'path saving images after cropping'

    # image_input = r'E:\ImageCrop\image_input'
    # image_output = r'E:\ImageCrop\image_output'

    images = os.listdir(image_input)
    image_crop(image_input, image_output, 0, 0, 1800, 1400)

