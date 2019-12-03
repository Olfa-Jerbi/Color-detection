import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

Result=cv2.imread("Result.png")

#Green channel seperately
plt.plot()
plt.title('G channel')
plt.ylabel('Height {}'.format(Result.shape[0]))
plt.xlabel('Width {}'.format(Result.shape[1]))
plt.imshow(Result[ : , : , 1])
plt.show()

#Red channel seperately
plt.plot()
plt.title('R channel')
plt.ylabel('Height {}'.format(Result.shape[0]))
plt.xlabel('Width {}'.format(Result.shape[1]))
plt.imshow(Result[ : , : , 2])
plt.show()

#Blue channel seperately
plt.plot()
plt.title('B channel')
plt.ylabel('Height {}'.format(Result.shape[0]))
plt.xlabel('Width {}'.format(Result.shape[1]))
plt.imshow(Result[ : , : , 0])
plt.show()
