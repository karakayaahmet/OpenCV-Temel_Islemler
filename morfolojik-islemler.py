import numpy as np
import cv2

img = cv2.imread("heli.jpg",0)
kernel = np.ones((5,5), np.uint8) 

erosion = cv2.erode(img,kernel, iterations=1)

dilation = cv2.dilate(img,kernel, iterations=1)

open = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("img",img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("morphology-open",open)
cv2.imshow("morphology-close", closing)
cv2.imshow("morphology-gradient", gradient)
cv2.imshow("morphology-tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
