import numpy as np
import math
import cv2

original=cv2.imread("Kindred.png")
contrast=cv2.imread("low_newskin.bmp")

def psnr(img1, img2):
    mse=np.mean((img1-img2)**2)     #mean square error
    print("MSE :", mse)

    if mse==0:
        return 100

    PIXEL_MAX=255.0

    return 20*math.log10(PIXEL_MAX/math.sqrt(mse))

result=psnr(original, contrast)
print("PSNR :", result)