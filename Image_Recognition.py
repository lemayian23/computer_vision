#Load references and test images in grayscale

reference_image = cv2.imread("Ngumbau lectures", cv2.IMREAD_GRAYSCALE) #Known image

test_image = cv2.imread("Ngumbau inro to Comp vision") # Image to recognize

orb = cv2.ORB_CREATE()

#Detect keypoints and compute