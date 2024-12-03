import numpy as np
import matplotlib.pyplot as plt

def read(name):
    return np.loadtxt(name)

def filter(data):
    cumsum_data = np.cumsum(data)
    filtred_data = np.zeros_like(data)
    filtred_data[:9] = cumsum_data[:9] / (np.arange(1, 10))
    filtred_data[9:] = (cumsum_data[9:] - cumsum_data[:-9]) / 10
    return filtred_data

def draw(data, filtred_data, save_name):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    ax1.plot(data)
    ax1.set_title('Original Data')
    ax2.plot(filtred_data)
    ax2.set_title('Filtered Data')
    plt.tight_layout()
    plt.savefig(save_name)
    plt.show()

def complete_task(file_name, save_name):
    data = read(file_name)
    filtred_data = filter(data)
    draw(data, filtred_data, save_name)

file_name = 'signal01.dat'
save_name = 'Task2_Result3.png'

complete_task(file_name, save_name)
