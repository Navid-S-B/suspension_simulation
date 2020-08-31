"""
Created on 5/08/2019

@author: Navid Bhuiyan
    
Purpose:
--------
   This function is used determinine the minimum and maximum discomfort values for 
   given damper and inerter coefficients by using a function to sort through any 
   given discomfort array. The minimum values will be the smallest discomfort value 
   for any given damper and inerter coefficent, but the maximum valuse will have 
   to be less than or equal to a upper discomfort limit. The function will only output 
   the associated damper and inerter coefficients.

Inputs:
-------    
    discomfort_array:
        - 2-dimentional float64 array with discomfort values for 
          given inerter and damping coefficients.
    
    inerter_array:
        -  A float64 linear array of inerter coefficients.
        
    damping_coefficient_values:
        -  A float64 linear array of damping coefficients.
    
    discomfort_upper_limit:
        - The conditional limit used to find the maximum discomfort value.
   
Output:
-------
    min_inerter and min_damping_coefficient:
        - The pair of coefficients that gives the smallest value of discomfort.  
    
    max_inerter and max_damping_coefficient:
        - The pair that gives the worst value of discomfort. 
        - This correlating discomfort value less than or equal to a given 
          'discomfort_upper_limit'.
"""
#import numpy library for array analysis.
import numpy as np

def optimise_qc(discomfort_array, inerter_array, damping_coefficient_array, discomfort_upper_limit):
    #Finding min discomfort.
    min_discomfort = np.min(discomfort_array)
    min_inerter_index,min_damping_index = np.where(discomfort_array==min_discomfort)
    min_inerter = float(inerter_array[min_inerter_index])
    min_damping_coefficient = float(damping_coefficient_array[min_damping_index])
    #Finding max discomfort with discomfort_upper_limit condition.
    discomfort_array_adjusted = discomfort_array[discomfort_array<=discomfort_upper_limit]
    max_discomfort = np.max(discomfort_array_adjusted)
    max_inerter_index, max_damping_index = np.where(discomfort_array==max_discomfort)
    max_inerter = float(inerter_array[max_inerter_index])
    max_damping_coefficient = float(damping_coefficient_array[max_damping_index])
    #Output
    return min_inerter, min_damping_coefficient, \
           max_inerter, max_damping_coefficient