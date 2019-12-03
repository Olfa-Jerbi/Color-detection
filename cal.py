import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

green=cv2.imread("sep_g.png")
red=cv2.imread("sep_r.png")
blue=cv2.imread("sep_b.png")
int_1=((float(format(green.mean())) + float(format(red.mean())) + float( format(blue.mean()))) /3)/255
print( int_1)
