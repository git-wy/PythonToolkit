# -*- coding: utf-8 -*-
# Author: Wendy WANG
# Modified: 12/30/2024

from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'opencv-python',
    ],
    author='Wendy WANG',
    description='Image Processing Toolkit',
    include_package_data=True,
    package_data={
        'image_processor': ['data_sample/*']
    }
)
