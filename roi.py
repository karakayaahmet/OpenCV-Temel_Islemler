import numpy as np
import cv2

# roi : region of interest : ilgi alanı

img = cv2.imread("cedric.jpg")

# print(img.shape)

roi = img[20:360 , 350:600]

cv2.imshow("roi",roi)

cv2.imshow("cedric", img)
cv2.waitKey(0)
cv2.destroyAllWindows()