from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import urllib

from keras.models import load_model
from matplotlib import pyplot
from numpy.random import randint

from PIL import Image
from urllib import request
from io import BytesIO
from model.instancenormalization import InstanceNormalization


from backend.settings import BASE_DIR
# load the models
cust = {'InstanceNormalization': InstanceNormalization}
model_BtoA = load_model(str(BASE_DIR) +  '\\model\\trained\\g_model_BtoA_001930.h5', cust)



# url = "https://llandscapes-10674.kxcdn.com/wp-content/uploads/2018/04/landscape-photography-portfolio-5.jpg"
# res = request.urlopen(url).read()
# Sample_Image = Image.open(BytesIO(res)).resize((256,256))


def convertImg(img):
    ##########################
    #Load a single custom image
    test_image = load_img(img, target_size=(256,256))
    test_image = img_to_array(test_image)
    test_image_input = np.array([test_image])
    test_image_input = (test_image_input - 127.5) / 127.5


    monet_generated  = model_BtoA.predict(test_image_input)
    images = vstack((monet_generated))
    images = (images + 1) / 2.0
    pyplot.imsave('img.png', images)
