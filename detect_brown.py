import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
image= cv2.imread("b.png")
dst= cv2.imread("white.png")
Result=cv2.imread("Result.png")
#Transforming the image from RGB to HSV 
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#boundaries in HSV
#lower_brow = np.array([10, 100, 20])
#upper_brow = np.array ([20, 255, 200])

bound=[  ( [10, 100, 20] , [20, 255, 200])]


#generating the image detecting the brown
for (lower,upper) in bound:
    lower=np.array(lower, dtype="uint8")
    upper=np.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)
    output= cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("images", np.hstack([image,output]))

    tmp = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(output)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)
    #cv2.imshow('funny',dst)
    cv2.imwrite("res.png", dst)
    print('Image size {}'.format(output.size))
    print('Maximum RGB value in this image {}'.format(output.max()))
    print('Minimum RGB value in this image {}'.format(output.min()))
    

#Results
#cv2.imshow("original image" , image)
#cv2.imshow("Detection", mask )

cv2.waitKey(0)
cv2.destroyAllWindows()














