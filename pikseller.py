import numpy as np
import cv2

img = cv2.imread("cedric.jpg")

dimension = img.shape
print(dimension)              #boyut bilgisi

color = img[420,500]
print("BGR: ",color)

blue = img[420,500,0]
print("blue: ",blue)

green = img[420,500,1]
print("green: ",green)

red = img[420,500,2]
print("red",red)

# mavi rengi değiştirme
img[420,500,0] = 250
print("yeni mavi: ",img[420,500,0])

# renk değişimi ikinci yöntem
blue1 = img.item(150,200,0)
print("blue1: ",blue1)

img.itemset((150,200,0),190)
print("yeni blue1: ",img[150,200,0])

cv2.imshow("cedric color",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
