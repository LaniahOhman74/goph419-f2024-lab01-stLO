"""
Compute the Launch angle range function of the ratio of escape velocity to terminal velocity, the desired maximum altitude as a fraction of Earth's radius, and the tolerance for maximum altitude


    Inputs
    --------
    ve_v0 : float
    alpha: float 
    tol_alpha: float

        The argument of the launch angle range function. 
    
    Returns
    ---------
    Array (2D)
        The range of the launch angle function
    
    Notes
    --------
    We are using the NumPy docstring format.
"""
import numpy as np

from Launch_Angle import launch_angle

def launch_angle_range(ve_v0, alpha, tol_alpha):
    #Empty list
    x = [] 
    #Minimum allowable launch angle, max alpha
    min_launchangle = (1+tol_alpha)*alpha
    x.append(launch_angle(ve_v0, min_launchangle))
    #Maximum allowable launch angle, min alpha
    max_launchangle = (1-tol_alpha)*alpha
    x.append(launch_angle(ve_v0, max_launchangle))
    v = np.array(x)
    return v


