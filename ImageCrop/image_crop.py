# -*- coding: utf-8 -*-
# Author: W.Y.
# Date: 2022/6/2

from PIL import Image
import os
import img2pdf


if __name__ == '__main__':

    input_path = r'E:\Users\ying wang\Downloads\iCloud 照片'
    output_path = r'E:\Users\ying wang\Desktop\新建文件夹'

    images = os.listdir(input_path)
    BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN = 170, 130, 1890, 1420

    for each_image in images:

        image_input_fullname = input_path + '/' + each_image
        img = Image.open(image_input_fullname)
        box = (BOX_LEFT, BOX_UP, BOX_RIGHT + BOX_LEFT, BOX_DOWN + BOX_UP)
        image_crop = img.crop(box)
        image_output_fullname = output_path + '/' + each_image
        image_crop.save(image_output_fullname)

        print('{} done.'.format(each_image))

    pdf_name = output_path + '/' + 'all.pdf'

    with open(pdf_name, "wb") as f:
        f.write(img2pdf.convert(
            [os.path.join(output_path, file) for file in images]))
