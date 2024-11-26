from PIL import Image
import numpy as np
import math

def processing(data):
    x,y = data.shape
    dif = math.ceil(255 / (np.amax(data) - np.amin(data)))
    min = np.amin(data)
    for i in range(x):
        for j in range(y):
            data[i][j]=(data[i][j]-min)*dif
    return data

def create_photo(image,saving_image_name):
    jpg = Image.open(image)
    data = np.array(jpg)
    result = processing(data)
    res_img = Image.fromarray(result)
    res_img.save(saving_image_name)

image = "lunar03_raw.jpg"
saving_image_name = "Task1_Result3.jpg"

create_photo(image,saving_image_name)
