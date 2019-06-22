import cv2
import numpy as np 
import matplotlib.pyplot as plt

image = cv2.imread("pika.png",1)

def binarize(img):
    img[img<150] = 255
    img[img<255] = 0
    return img

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = binarize(image)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.show()