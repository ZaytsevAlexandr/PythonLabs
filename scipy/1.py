import sympy as sp

r, m, l = sp.symbols('r m l')
A = sp.Matrix([[0, 0, 0, - 1 / r, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, - 1 / r, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, - 1 / r, 0, 0, 0],
               [-(l + m * 2), 0, 0, 0, 0, 0, 0, 0, 0],
               [0, -m, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, -m, 0, 0, 0, 0, 0, 0],
               [-m, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [-m, 0, 0, 0, 0, 0, 0, 0, 0]])

eig = A.eigenvals()

# a, b, c = map(float, input().split())
# eig_values = A.subs({r: a, m: b, l: c}).eigenvals()

print(eig)
# print(eig_values)
