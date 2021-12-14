import numpy as np
import glob, os, os.path
from cv2 import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('E:/exam projects/myproject/maching fecher/ph1.jpg',0) # queryImage
img2 = cv2.imread('E:/exam projects/myproject/maching fecher/ph2.jpg',0) # trainImage

# Initiate SIFT detector
sift = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
	# BFMatcher with default params
bfg = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
matches = bfg.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
	
img_out = cv2.drawMatches(img2, kp2, img1, kp1,
				matches[:20], None, flags=2)
	
plt.imshow(img_out)
plt.show()