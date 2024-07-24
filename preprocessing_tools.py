import cv2 as cv
import numpy as np


#take an image(np array) and adds the padding, the user can choose both the value of the pixels (zero by default) and the padding size (assuming 1 if not specified)
def padding(img, value=0, size=1):
    padded_img = np.pad(img, pad_width=size, mode='constant', constant_values=value)
    return padded_img

class filter2D:
    def __init__(self,effect):
        pass


