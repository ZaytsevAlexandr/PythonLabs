import numpy as np
import matplotlib.pyplot as plt

def read(name):
    data=np.array([])
    with open(name, 'r') as file:
        for line in file:
            data=np.append(data,float(line.strip()))
    return data

def filter(data):
    filtred_data=np.array([])
    for i in range (len(data)):
        if (i<9):
            filtred_data=np.append(filtred_data,np.average(data[0:(i+1)]))
        else:
            filtred_data=np.append(filtred_data,np.average(data[i-9:(i+1)]))
    return filtred_data

def draw(data, filtred_data, save_name):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # 1 ряд, 2 столбца

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
