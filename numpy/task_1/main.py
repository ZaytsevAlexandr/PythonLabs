from PIL import Image
import numpy as np
import math

def processing(data):
    min_val = np.amin(data)
    max_val = np.amax(data)
    
    dif = 255 / (np.amax(data) - np.amin(data))
    
    data = (data - np.amin(data)) * dif
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
