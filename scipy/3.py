import sympy as sp
from scipy import integrate
from matplotlib import pyplot as plt
import numpy as np

x = sp.symbols('x')
y = sp.Function('y')

equation = sp.Eq(y(x).diff(x), -2 * y(x))

solution = sp.dsolve(equation, ics={y(0): 2 ** 0.5})

inter = np.linspace(0, 10, 100)

y_solution = solution.rhs
ans = sp.lambdify(x, y_solution, 'numpy')
y_ans = ans(inter)

def f(x, y):
    return -2 * y

sol = integrate.solve_ivp(f, (0, 10), [2 ** 0.5], t_eval=inter)

plt.figure()
plt.scatter(sol.t, sol.y)
plt.plot(inter, y_ans, color='orange')
plt.grid()

plt.figure()
plt.scatter(inter, np.array(sol.y) - y_ans)
plt.grid()
plt.show()
