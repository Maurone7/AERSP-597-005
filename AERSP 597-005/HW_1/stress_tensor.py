# Importing necessary libraries
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

# Defining symbols
x, y, z = sym.symbols('x y z')
C_1, C_2 = sym.symbols('C_1 C_2')
E, v = sym.symbols('E v')
L = sym.symbols('L')

# Defining displacement function
w = C_1*sym.sin(sym.pi*x/L)*sym.sin(sym.pi*y/L)
u = C_2*x

# Calculating stress tensor
tilde_sigma = sym.Matrix([sym.diff(u, x), 0, 0]) - z*sym.Matrix([sym.diff(sym.diff(w, x), x), 0, 0])
print(tilde_sigma)

# Defining compliance matrix
compliance_matrix = sym.Matrix([[E/(1-v**2), v*E/(1-v**2), 0],[v*E/(1-v**2), E/(1-v**2), 0],[0, 0, E/(2*(1+v))]])

# Calculating stress matrix
stress = compliance_matrix*tilde_sigma

# Calculating the inside of the integral
inside_of_integral = sym.Transpose(tilde_sigma)*stress

# Printing the result
print(inside_of_integral)

integral = sym.integrate(sym.integrate(inside_of_integral[0], (x, 0, L)), (y, 0, L))
print(integral)
