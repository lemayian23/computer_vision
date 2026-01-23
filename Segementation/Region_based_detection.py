#This groups pixels into  regions based on predefined criteria such as intesity values or texture
#The idea is to group neighboring pixels pixels with similar properties into same regions
#Common methods are: Region growing and watershed

#Apply watershed algorithm
import numpy as np

#convert image to binary
_, binary = cv2.threshold(image, 0, 255,cv2.THRESHOLD_BINARY_INV + cv2.THRESHOTSU)
#Perform distance transform
distance_transform = cv2.distanceTransform(binary_image, cv2.DIST_L2, 5)
_, foreground = cv2.threshold(distance_transform, 0.7 * distance_transform.max(), 255, 0)
foreground - np.uint8(foreground)
unknown = cv2.connectedComponents(foreground)
#Marker labeling
_, markers = cv2.connectedComponents)foreground)
markers = markers +1
markers[unknown == 255] = 0
#Apply watershed
markers = cv2.watershed(image, markers)
image[markers=== -1] = [255, 0, 0]