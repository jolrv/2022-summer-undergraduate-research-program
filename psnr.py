import numpy as np
import math
import cv2

original=cv2.imread("Kindred.png")
compressed=cv2.imread("low_newskin.bmp")

def PSNR(original, compressed):
    mse=np.mean((original-compressed)**2)     #mean square error

    if mse==0:
        return 100

    max_pixel=255.0
    psnr=20*math.log10(max_pixel/math.sqrt(mse))

    return psnr

result=PSNR(original, compressed)
print("PSNR :", result, "db")
