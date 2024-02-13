from sympy import integrate, symbols, exp, sqrt, pi
from sympy.utilities import lambdify
import sympy as sp

def sigma_z(M_x, M_y, I_xx, I_yy, I_xy):
    sigma_z_x = (M_y * I_xx - M_x * I_xy)/ (I_xx * I_yy - I_xy**2)
    sigma_z_y = (M_x * I_yy - M_y * I_xy)/ (I_xx * I_yy - I_xy**2)
    return sigma_z_x, sigma_z_y

I_xy = -808 - 898
I_xx = 912 + 1968
I_yy = 2059 + 820
print(sigma_z(10000, 0, I_xx, I_yy, I_xy))
def virtual_displacement(sigma_z):
    z = symbols('z')
    sigma_z_x, sigma_z_y = sigma_z
    print(sigma_z_x, sigma_z_y)
    c_1, c_2, c_3, c_4 = symbols('c1 c2 c3 c4')
    u_prime = str(integrate(sigma_z_x, z)) + str(c_1)
    print("u'", u_prime)
    v_prime = str(integrate(sigma_z_y, z)) + str(c_3)
    print("v'", v_prime)
    return u_prime, v_prime

virtual_displacement(sigma_z(10000, 0, I_xx, I_yy, I_xy))

sigma_z_x, sigma_z_y = sigma_z(10000, 0, I_xx, I_yy, I_xy)
z, c_1, c_2 = symbols('z c1, c2')
u_prime = integrate(sigma_z_x, z)