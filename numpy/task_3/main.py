import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from PIL import Image

def read(name):
    data = np.array([])
    with open(name) as f:
        for line in f:
            data = np.append(data,[float(x) for x in line.split()])
    data = np.expand_dims(data, axis=1)
    return data

def create_matrix(n):
    A = np.zeros((n, n))
    np.fill_diagonal(A, 1)
    A[np.arange(n), (np.arange(n) - 1) % n] = -1
    return A

def create_gif(step, data, A, save_name):
    frames = []
    for i in range(step):
        plt.figure()
        plt.grid(True) 
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.plot(data)
        plt.ylim(0, 10)
    
        plt.savefig('temp.png')
        product = np.dot(A, data)
        data = data - 0.5 * product
        plt.close() 
    
        frame = Image.open('temp.png')
        frames.append(frame)
    
    frames[0].save(save_name, save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)
    
    import os
    os.remove('temp.png')

def complete_task(name,step,save_name):
    data = read(name)
    A = create_matrix(np.size(data))
    create_gif(step, data, A, save_name)

name = 'data.txt'
step = 255 
save_name = "animation.gif"

complete_task(name, step, save_name)
