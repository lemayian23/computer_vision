#this converts a grayscale image into binary by setting a tthreshold value

#pixels with intensity values above the threshold are assigned one value(e.g black)
# and those below the threshold are assigned another value)e.g white)

import cv2

#Load image in grayscale
image =  cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH.BINARY)

#Adaptive thresholdhing(one which uses diff values for different image regions)

adaptive_binary_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)