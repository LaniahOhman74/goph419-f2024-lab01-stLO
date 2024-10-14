import sys
import unittest 
import math 
import numpy as np
#sys.path.append(r"C:\Users\lania\Documents\GOPH419 Lab Codes\goph419-f2024-lab01-stLO\min_max_angles\arcsin(x).py")
from Sineinverse import arcsin
def sinversetest():
    x = 0.5
    print(f"{x} = {arcsin(x)}")

    x = 0.7 
    print(f"{x} = {arcsin(x)}")

from Launch_Angle import launch_angle
def launchangletest():
    ve_v0 = 2.0
    alpha = 0.25

    print(launch_angle(ve_v0, alpha))

from Launch_Angle_Range import launch_angle_range
def launchanglerangetest():
    ve_v0 = 2.21
    alpha = 0.25
    tol_alpha = 0.02
    print(launch_angle_range(ve_v0, alpha, tol_alpha))

sinversetest()
launchangletest()
launchanglerangetest()

if __name__ == "main":
    main()