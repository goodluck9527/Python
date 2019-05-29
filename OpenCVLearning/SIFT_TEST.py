"""
Created on Sat Sep 29 14:43:02 2018

@author: qgl
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

imgname = 'C:/Users/qgl/Desktop/articles/test1.jpg'

sift = cv2.xfeatures2d.SIFT_create()

img = cv2.imread(imgname)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kp,des = sift.detectAndCompute(img, None)

cv2.imshow('gray',gray)
cv2.waitKey(0)

img1=cv2.drawKeypoints(img,kp,img,color=(255,0,255))

cv2.imshow('point',img1)
cv2.waitKey(0)