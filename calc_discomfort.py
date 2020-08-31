"""
Created on 5/08/2019

@author: Navid Bhuiyan

Purpose:
--------
   Determines the discomfort level for a specific verticle velocity of the quarter
   car body i.e. variable vs which is calculated from the function simulate_qc, using
   a set of specific parameters as explained in simulate_qc.

Inputs:
-------
    vs - the verticle velocity of the quarter car body.       
    dt - time increment. 

Output:
-------
   discomfort: 
       - A scalar value representing the discomfort level for the given
         vehicle and suspension parameters.       
"""
#import numpy library for useful functions.
import numpy as np

def calc_discomfort(vs,dt):
    #Considered all the calculations for discomfort
    #into one line of code.
    discomfort = float(np.sum((np.diff(vs)/dt)**2))
    return discomfort