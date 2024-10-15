'''
Inputs:
--------------------
alpha - altitude in reference to Earths radius 
ve_v0 - velocity ratio
tol_alpha - tolerance altitude

Results:
--------------------
Pass or fail, fail raises a value error
Checks if system is working 

Notes
---------------------
Tests check that definition run correctly
For launch angle range it checks the code for a negative velocity ratio
A negative altitude 
As well as for a situation where the squareroot value in euqation 17 is negative

'''
import sys
import unittest 
import math 
import numpy as np
#sys.path.append(r"C:\Users\lania\Documents\GOPH419 Lab Codes\goph419-f2024-lab01-stLO\min_max_angles\arcsin(x).py")
from Sineinverse import arcsin
def sinversetest():
    x = 0.5
    print(f"{x} = {arcsin(x)}", 'This agrees with what was expected', np.arcsin(0.5))

    x = 0.7 
    print(f"{x} = {arcsin(x)}", 'This agrees with what was expected', np.arcsin(0.7))

    x = 1
    print(f"{x} = {arcsin(x)}",'This does not pass, expected value to be', np.arcsin(1))

from Launch_Angle import launch_angle

def launchangletest():
    ve_v0 = 2.0
    alpha = 0.25

    print('Pass', launch_angle(ve_v0, alpha))

from Launch_Angle_Range import launch_angle_range
def launchanglerangetest():
    #Runs perfectly
    ve_v0 = 2.00
    alpha = 0.25
    tol_alpha = 0.02
    print('Pass',launch_angle_range(ve_v0, alpha, tol_alpha))

def launchanglerangetest1():
#ve_v0 is negative, fails
    ve_v0 = -2.00
    alpha = 0.25
    tol_alpha = 0.02
    print('Fail', launch_angle_range(ve_v0, alpha, tol_alpha))    

def launchanglerangetest2():
#alpha is negative, fails  
    ve_v0 = 2.00
    alpha = -0.25
    tol_alpha = 0.02
    print('Fail', launch_angle_range(ve_v0, alpha, tol_alpha))      

def launchanglerangetest3():
#Squareroot of equation 17 is negative, fails
    ve_v0 = 2.00
    alpha = 100
    tol_alpha = 0.02
    print('Fail', launch_angle_range(ve_v0, alpha, tol_alpha))

sinversetest()
launchangletest()
launchanglerangetest()
launchanglerangetest1()
launchanglerangetest2()
launchanglerangetest3()