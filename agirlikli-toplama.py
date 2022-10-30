import cv2
import numpy as np

circle = np.zeros((512,512,3), np.uint8) + 255
cv2.circle(circle, (256,256), 60, (255, 0, 0), -1)

rec = np.zeros((512,512,3), np.uint8) + 255
cv2.rectangle(rec, (150,150), (350,350), (0,0,255), -1)

dst = cv2.addWeighted(circle, 0.7, rec, 0.3, 20)

cv2.imshow("circle", circle)
cv2.imshow("rec", rec)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()