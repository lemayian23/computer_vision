# it groups pixels into clusters based on their similarity.based
#K-means is a popular method
import numpy as np

#Convert image to float32
image = np.float32(image)
#Define criteria and apply k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
_, labels, centers = cv2.kmeans(image, 3, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
#Convert back to uint8 and reshape the image
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape((image.shape))