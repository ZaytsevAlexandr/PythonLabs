import numpy as np
import matplotlib.pyplot as plt

f = open('005.dat', 'r')
N = int(f.readline()[0:-1])
data_x=np.array([0] * N)
data_y=np.array([0] * N)
for i in range (N):
    data = f.readline()[0:-1].split(" ")
    data_x[i]=float(data[0])
    data_y[i]=float(data[1])

plt.scatter(data_x, data_y, s=20, color='purple')
plt.title("Визуализация %d точек" %N)
plt.xlabel('Значения по координате x')
plt.ylabel('Значения по координате y')
plt.grid(which='minor', linewidth=0.3, linestyle='--')
plt.minorticks_on()
plt.grid()
plt.savefig('task1_plot5.png')
plt.show()
