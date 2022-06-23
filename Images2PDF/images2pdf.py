# -*- coding: utf-8 -*-
# Author: Ying Wang

import os
import img2pdf


if __name__ == '__main__':

    image_input = r'path saving images'
    pdf_output = r'pdf file'

    # image_input = r'E:\Images2PDF\image_input'
    # pdf_output = r'E:\Images2PDF\output.pdf'

    images = os.listdir(image_input)

    with open(pdf_output, "wb") as f:
        f.write(img2pdf.convert(
            [os.path.join(image_input, image) for image in images]))

    print(f'Successfully save all images to {pdf_output}!')
