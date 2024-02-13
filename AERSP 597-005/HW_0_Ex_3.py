import numpy as np
import sys

sigma_11, sigma_12, sigma_13 = 100, 10, 20
sigma_21, sigma_22, sigma_23 = 10, -100, 0
sigma_31, sigma_32, sigma_33 = 20, 0, 50

matrix = np.array([[sigma_11, sigma_12, sigma_13], [sigma_21, sigma_22, sigma_23], [sigma_31, sigma_32, sigma_33]])
print(matrix)

I_1 = sigma_11 + sigma_22 + sigma_33
I_2 = sigma_11 * sigma_22 + sigma_22 * sigma_33 + sigma_33 * sigma_11 - (sigma_12 ** 2) - (sigma_23 ** 2) - (sigma_31 ** 2)
I_3 = sigma_11 * sigma_22 * sigma_33 - sigma_11 * (sigma_23 ** 2) - sigma_22 * (sigma_31 ** 2) - sigma_33 * (sigma_12 ** 2) + 2 * sigma_12 * sigma_23 * sigma_31

#I_1, I_2, I_3 = (np.linalg.eig(matrix))[0]
print(I_1, I_2, I_3)

phi = 1/3*np.arccos((2*I_1**3 -9*I_1*I_2 +27*I_3)/(2*(I_1**2 -3*I_2)**(3/2)))
print(phi)

sigma_I = I_1/3 +2/3*np.sqrt(I_1**2 -3*I_2)*np.cos(phi)
sigma_II = I_1/3 +2/3*np.sqrt(I_1**2 -3*I_2)*np.cos(phi - 2*np.pi/3)
sigma_III = I_1/3 +2/3*np.sqrt(I_1**2 -3*I_2)*np.cos(phi - 4*np.pi/3)
print(sigma_I, sigma_II, sigma_III)

sigma_e = np.sqrt(((sigma_I - sigma_II)**2 + (sigma_II - sigma_III)**2 + (sigma_III - sigma_I)**2)/2)
print(sigma_e)
