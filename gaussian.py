import cv2
import numpy as np
from PIL import Image

im=Image.open('Kindred.png')    #Image load
im_array=np.asarray(im)     #Image to np.array

# img=cv2.imread("cat.png")
# cv2.imshow("CAT", img)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

kernel1d=cv2.getGaussianKernel(5, 3)
kernel2d=np.outer(kernel1d, kernel1d.transpose())

low_im_array=cv2.filter2D(im_array, -1, kernel2d)   #consolve
high_im_array=im_array-low_im_array+128

low_im=Image.fromarray(low_im_array)    #np.array to Image
high_im=Image.fromarray(high_im_array)

low_im.save('low_newskin.bmp', 'BMP')
high_im.save('high_newskin.bmp', 'BMP')
# print(kernel2d)