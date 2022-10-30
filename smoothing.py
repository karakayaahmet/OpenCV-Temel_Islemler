import numpy as np
import cv2

img_filter = cv2.imread("filter.png")
img_median = cv2.imread("median.png")
img_bilateral = cv2.imread("bilateral.png")

blur = cv2.blur(img_filter,(5,5)) #pozitif tek sayılar olmalı!
blur2 = cv2.GaussianBlur(img_filter,(5,5), cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median,7)
blur_b = cv2.bilateralFilter(img_bilateral,9,95,95)

cv2.imshow("filter", blur)
cv2.imshow("imgfilter", img_filter)
cv2.imshow("Gaussianblur",blur2)
cv2.imshow("medianblur", blur_m)
cv2.imshow("original median",img_median)
cv2.imshow("original bilateral",img_bilateral)
cv2.imshow("blurb",blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()