
#It uses convolutional neural networks(CNNs) to segment images and is very accurate and can handle comple images

#Common models are: Fully CNNs and U-Net

from keras.models import Model
from keras.layers import Input, Con2D, MaxPooling2D, UpSampling2D, concatenate

inputs = Input((Image_height, image_width, 1))
conv1 = Conv2D(64, 3, activation = 'relu', padding = 'same')(inputs)
pool1 = MaxPooling2D((pool_size= 2, 2))(conv1)
conv2 = Conv2D (128, 3, activation = 'relu', padding = 'same')(pool1)
up1 = concatenate([UpSampling2D(size =(2, 2))(conv2), conv1], axis = 3)
conv3 = Conv2D(1,1, activation = 'relu', padding = 'same')(up1)
outputs = Con2D(1, 1, activation = 'sigmoid')(conv3)
model = Model(inputs= [inputs], outputs = [outputs])