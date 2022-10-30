import cv2
import numpy as np

img = cv2.imread("heli.jpg",0)
row,col = img.shape

m = np.float32([[1,0,10],[0,1,10]])

dst = cv2.warpAffine(img,m,(row,col))

cv2.imshow("original",img)
cv2.imshow("yeni",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()