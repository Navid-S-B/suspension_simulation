"""
Created on 5/08/2019

@author: Navid Bhuiyan
    
Purpose:
--------
   Determines the discomfort values for given damper and inerter values
   coefficients, and then outputting the results in a float64 array.

Inputs:
-------
    time_array - a float64 array of given time values.
    y_road - a float64 array of road heights.
    ms - the mass of 1/4 of the car body.
    mu - the mass of the tyre and wheel.
    kt - tyre stiffness.
    k - spring stiffness.
    inerter_values - a float64 array containing inertance values.
    damping_coefficient_values - a float64 array of damping coefficient values.

Output:
-------
   discomfort_array:
       - 2-dimentional float64 array with discomfort values for 
         given damper and inerter coefficients.
"""

import numpy as np
import calc_discomfort as cd
import simulate_qc as sqc

def explore_qc(time_array, y_road, ms, mu, kt, k, 
               inerter_array, damping_coefficient_array):
    #Find the time difference.
    dt = time_array[1]-time_array[0]
    #Generate empty discomfort_array correlating to the sizes of the inerter_array
    #and damping_coefficient_array. Also setting the array to be of type float64
    #for the computation of float values.
    discomfort_array = np.zeros((len(inerter_array), len(damping_coefficient_array)), dtype=np.float64)
    #For loop designed to fill the discomfort_array row-wise.
    for i in range(len(inerter_array)):
        for j in range(len(damping_coefficient_array)):
            #Calculate vs for given inerter and damping coefficient.
            ys, yu, vs, vu = sqc.simulate_qc(time_array, y_road, ms, mu, kt, k, inerter_array[i], \
                             damping_coefficient_array[j])
            #Assign the discomfort value to its correlating coefficients.
            discomfort_array[i,j]=cd.calc_discomfort(vs,dt)
    return discomfort_array

