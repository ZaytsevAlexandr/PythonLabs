from scipy.linalg import solve
from matplotlib import pyplot as plt

f = open('2.txt', 'r')
a = f.read().split('\n')
f.close()

n = int(a[0])
A = []
x = []
for i in range(n):
    A.append([float(j) for j in a[i + 1].split(' ')])
    x.append(i)

b = [float(j) for j in a[n + 1].split(' ')]

ans = solve(A, b)

plt.bar(x, ans)
plt.grid()
plt.show()
