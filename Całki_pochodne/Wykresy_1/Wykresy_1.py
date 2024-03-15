import math
import numpy as np
import matplotlib.pyplot as plt

#Installation:
# In Solution Explorer
# <Project name> -> Python Environments
# RMB on Python Environments -> View all Python Environments -> Packages(PyPl) -> search and install packages

#def f(x):
#    return x**0.5 + 1

#x = np.linspace(2, 16)
#plt.plot(x, f(x), color='black')

#plt.show()

def f(x):
    return x**2 - 3 * x - 4

x = np.linspace(-7, 10)
plt.plot(x, f(x), color='black')
plt.show()

def calka(p, k, n):
    dx = (k - p) / n
    suma = 0
    for i in range(n):
        suma += f(p + i * dx + dx / 2) * dx
    return suma

print(calka(4, 6, 4))
