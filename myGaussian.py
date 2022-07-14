import cv2
import numpy as np
import math
from PIL import Image

def get_gaussian_filter_1d(size, sigma):
    """
    generate 1D gaussian filter
    :param size: int kerner size
    :param sigma: float
    :return: np.array
    """
    assert size%2==1, "Filter Dimension must be odd"
    arr=np.arange(math.trunc(size/2)*(-1), math.ceil(size/2)+1, 1)
    kernel_raw=np.exp((-arr*arr)/(2*sigma*sigma))
    kernel=kernel_raw/kernel_raw.sum()

    return kernel

im=Image.open('Kindred.png')
im_array=np.asarray(im)

kernel1d=get_gaussian_filter_1d(5, 3)
kernel2d=np.outer(kernel1d, kernel1d.transpose())

low_im_array=cv2.filter2D(im_array, -1, kernel2d)
low_im=Image.fromarray(low_im_array)
low_im.save('made_low_newskin.bmp', 'BMP')