"""
Compute the Launch angle function of the ratio of escape velocity to terminal velocity and the desired maximum altitude as a fraction of Earth's radius.

    Inputs
    --------
    ve_v0 : float
    alpha: float 
        The argument of the launch angle function. 
    
    Returns
    ---------
    float
        The value of the launch angle function
    
    Notes
    --------
    We are using the NumPy docstring format.
"""
from Sineinverse import arcsin
import numpy as np
def launch_angle(ve_v0, alpha):
    if ve_v0 < 0:
        raise ValueError(f"Negative ve_v0: {ve_v0}")
    if alpha < 0:
        raise ValueError(f"Negative alpha: {alpha}") 
    z = (1 + alpha)*np.sqrt(1-((alpha/(1+alpha))*(ve_v0**2)))
    result = arcsin(z)
    return result 



                                
                          