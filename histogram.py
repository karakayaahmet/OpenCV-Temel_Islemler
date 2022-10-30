import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.zeros((500,500), np.uint8)
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)

img1 = cv2.imread("smile.jpg")
b,g,r = cv2.split(img1)

cv2.imshow("img",img)
cv2.imshow("img1",img1)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

# plt.hist(img1.ravel(),256,[0,256])
# plt.show()
# plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()