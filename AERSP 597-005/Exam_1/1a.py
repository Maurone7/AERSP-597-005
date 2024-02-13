import numpy as np

poisson_ratio = 0.1
yield_strenght = [220, -320]
ultimate_strenght = [305, -410]

#Set everyhting in MPa
E = 200 *10e3

sigma_x, sigma_y = 50, 150
tau_xy = 150

compliance_matrix = [[1/E, -poisson_ratio/E, 0],
                     [-poisson_ratio/E, 1/E, 0],
                     [0, 0, E/(2*(1+poisson_ratio))]]

print(compliance_matrix)
