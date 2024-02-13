import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

func1 = lambda x: 1-np.cos(2*np.pi*x/3)
func2 = lambda x: np.sin(np.pi*x/3)

x = sp.symbols('x')
func_1_prime = sp.utilities.lambdify(x, sp.diff(1-sp.cos(2*sp.pi*x/3), x))
func_2_prime = sp.utilities.lambdify(x, sp.diff(sp.sin(sp.pi*x/3), x))

x = np.linspace(0, 3, 100)
plt.plot(x, func1(x), label=r'$1-cos(\frac{2x\pi}{3})$')
plt.plot(x, func2(x), label=r'$sin(\frac{x\pi}{3})$')
plt.plot(x, func_1_prime(x), label=r'$1-cos(\frac{2x\pi}{3})$ prime')
plt.plot(x, func_2_prime(x), label=r'$sin(\frac{x\pi}{3})$ prime')
plt.legend()
plt.show()