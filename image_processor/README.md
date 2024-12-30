# Image Processing Toolkit
**Author**: Wendy WANG  
**Modified**: 12/30/2024

A toolkit to process images, such as resize images and convert images to other formats.

- How to install it?

```shell
pip install git+https://github.com/yingwendy-wang/Py_Toolkit.git#subdirectory=image_processor
```


## Table of Contents

- [Resize Images](#resize-images)
- [Convert Images to PDF](#convert-images-to-pdf)
- [Convert a handwriting image to a clear signature](#convert-a-handwriting-image-to-a-clear-signature)

## Resize Images

```python
from image_processor import resize_image

my_image_input = r'../image_input_folder/'  # a folder saving all images to be resized
my_image_output = r'../image_output_folder/'  # a folder saving all resized images

resize_image(my_image_input, my_image_output, mode='resize', size=(1190, 1490))
resize_image(my_image_input, my_image_output, mode='crop', crop_box=(0, 0, 300, 400))
```


## Convert Images to PDF

```python
from image_processor import image2pdf

my_image_input = r'../image_input_folder/'  # a folder saving all images
my_pdf_output = r'../my_pdf_output.pdf'  # a pdf file

image2pdf(my_image_input, my_pdf_output)
```


## Convert a handwriting image to a clear signature

- Sign on white paper with a black pen
- Take a photo of the signature and save it as `../img_to_signature.png`
- Run the following code


```python
from image_processor import image2signature

my_image = r'../img_to_signature.png'
my_signature = r'../my_signature_output.png'

image2signature(my_image, my_signature)
```
