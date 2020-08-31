"""
Created on 6/08/2019

@author: Navid Bhuiyan

Purpose:
--------    
    To simulate a quarter car based on the 
    model described in the assignment i.e. the quarter
    car model.

Inputs:
-------
   time_array - a float64 array of given time values.
   y_road - a float64 array of road heights
   ms - the mass of 1/4 of the car body
   mu - the mass of the tyre and wheel
   kt - tyre stiffness
   k - spring stiffness
   b - inertance
   c - damping coefficient

Outputs:
--------
  ys - the verticle displacement of the center of the car body
       from a reference level
  yu - the verticle displacement of the center of the wheel/tyre 
       from a reference level
  vs - the verticle velocity of the quarter car body       
  vu - the verticle velocity of the wheel/tyre
"""

#Import numpy library for simulation.
import numpy as np

def simulate_qc(time_array, y_road, ms, mu, kt, k, b, c):
    #Find time difference
    dt = time_array[1]-time_array[0]
    #Create empty arrays with the same size as the time_array. Also the initial 
    #condtions of ys(0)=0, yu(0)=0, vs(0)=0, and vu(0)=0 are accounted for as the 
    #following arrays are zero filled.
    ft = np.zeros_like(time_array)
    ht = np.zeros_like(time_array)
    ys = np.zeros_like(time_array)
    yu = np.zeros_like(time_array)
    vs = np.zeros_like(time_array)
    vu = np.zeros_like(time_array)
    #Simplification of formulae in the for-loop.
    den = ms*mu+(ms+mu)*b
    #For loop to simulate data for all the variables, used backward euler method 
    #as it provides better and more accurate results compared to the euler foward 
    #method. As m starts from one, it maintains the conditions of 
    #ys(0)=0, yu(0)=0, vs(0)=0, and vu(0)=0.
    for n in range(1,len(time_array)):
        ft[n-1] = c*vs[n-1] - c*vu[n-1] + k*ys[n-1] - k*yu[n-1]
        ht[n-1] = ft[n-1] - kt*yu[n-1] + kt*y_road[n-1]
        ys[n] = ys[n-1] + vs[n-1]*dt
        yu[n] = yu[n-1] + vu[n-1]*dt
        vs[n] = vs[n-1] + ((-(mu+b)*ft[n-1]+b*ht[n-1])/den)*dt
        vu[n] = vu[n-1] + ((-b*ft[n-1]+(ms+b)*ht[n-1])/den)*dt
    return ys,yu,vs,vu