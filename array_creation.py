import numpy as np

#Create blank image
blank = np.zeros((300,400,3), dtype=np.unint8)# 300*400 BGR

#Create white image
white = np.ones((300, 400, 3), dtype = np.uints8)* 255

#Create random image
random_img = np.random.randint(0,256, (300, 400, 3), dtype=np.uint8)

#Create gradient
gradient = np.linspace(0, 255, 400, dtype = np.uint8)
gradient_img = np.tile(gradient, (300, 1))
