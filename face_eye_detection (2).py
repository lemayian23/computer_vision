import cv2
import numpy as np

# Load classifiers
face_cascade = cv2.CascadesClassifier(
    cv2.data.haarcascades + 'haaarcarcade_frontalface_default.xml')
    