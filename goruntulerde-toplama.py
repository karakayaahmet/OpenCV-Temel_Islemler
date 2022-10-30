import cv2
import numpy as np

circle = np.zeros((512,512,3), np.uint8) + 255
cv2.circle(circle, (256,256), 60, (255,0,0), -1)

rec = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rec,(150, 150), (350, 350), (0,0,255), -1)

add = cv2.add(circle, rec)

cv2.imshow("circle",circle)
cv2.imshow("rectangle",rec)
cv2.imshow("add", add)

cv2.waitKey(0)
cv2.destroyAllWindows()