import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**0.5 + 1

x = np.linspace(-5, 16)
plt. plot(x, f(x), color='black')

plt.show()

# Metoda bisekcji
