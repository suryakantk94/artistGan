from os import listdir
import os
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




def convertImg(img, style):

    imgName = img.split(os.sep)[-1:][0]

    RES_IMG = os.path.join(BASE_DIR,'static','convert_img',imgName)

    #Load a single custom image
    test_image = load_img(img, target_size=(256,256))
    test_image = img_to_array(test_image)
    test_image_input = np.array([test_image])
    test_image_input = (test_image_input - 127.5) / 127.5

    if style == "Rajasthani":
        model_BtoA = load_model(os.path.join(BASE_DIR,'model','trained', 'g_model_BtoA_001930.h5'), cust)
    elif style == "Mathali":
        model_BtoA = load_model(os.path.join(BASE_DIR,'model','trained', 'g_model_BtoA_001930.h5'), cust)
    elif style == "Raja ravi verma":
        model_BtoA = load_model(os.path.join(BASE_DIR,'model','trained', 'g_model_BtoA_001930.h5'), cust)
    elif style == "Gond":
        model_BtoA = load_model(os.path.join(BASE_DIR,'model','trained', 'g_model_BtoA_001930.h5'), cust)

    monet_generated  = model_BtoA.predict(test_image_input)
    images = vstack((monet_generated))
    images = (images + 1) / 2.0
    # Save img

    pyplot.imsave(RES_IMG, images)

    return imgName
