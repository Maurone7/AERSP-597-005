import numpy as np

def center_of_mass(x_0, y_0, x, y):
    # x_0, y_0 are the coordinates the bottom left corner of the rectangle
    # x, y are the coordinates of the points
    # returns x_c, y_c the coordinates of the center of mass
    x_c = np.mean(x) + x_0
    y_c = np.mean(y) + y_0
    return x_c, y_c

def system_center_of_mass(length_list, initial_coordinates):
    # length_list is a list of lists, each containing the lengths of one rectangle
    x, y = length_list[0], length_list[1]
    x_0, y_0 = initial_coordinates[0], initial_coordinates[1]
    x_c, y_c = center_of_mass(x_0, y_0, x, y)
    x_c_sys = [sum(x_0[i] * (x[i] * y[i]))/sum((x[i] * y[i])) for i in range(len(length_list))]
    y_c_sys = [sum(y_0[i] * (x[i] * y[i]))/sum((x[i] * y[i])) for i in range(len(length_list))]

    return x_c_sys, y_c_sys

system_center_of_mass([1, 1], [0, 0])
