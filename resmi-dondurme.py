import cv2
import numpy as np

img = cv2.imread("heli.jpg",0)
row,col = img.shape

m = cv2.getRotationMatrix2D((col/2,row/2), 90, 1)

dst = cv2.warpAffine(img,m,(col,row))

cv2.imshow("original",img)
cv2.imshow("dondurme",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()