import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("heli.jpg")

ret,th1 = cv2.threshold(img,100,200, cv2.THRESH_BINARY)


cv2.imshow("img",img)
cv2.imshow("th",th1)

cv2.waitKey(0)
cv2.destroyAllWindows()