#Detects edges within an image and uses them to define boundaries of segments.an#The commn used method is Canny Edge Detector a multi-stage algo that detects a wide range of edges

edges = cv2.Canny(image, 100, 200)