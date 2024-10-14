#Function to determine the inverse sine
"""Compute the Sine function for scalar inputs.

    Inputs
    --------
    x : float
        The argument of the Sine function. 
    
    Returns
    ---------
    float
        The value of the Sine function
    
    Notes
    --------
    We are using the NumPy docstring format.

    #"What does this function do???"
    #Parameters
    #The right hand side of equation 17 must be equal to or less than 1, for the whole equation
    #Portion in the squareroot = x_not
    #Whole equation = x
    #The squareroot portion of the function must be greater than or equal to 0 (to determine a real number)
    """
import numpy as np
def arcsin(x):
    if x < -1 or x > 1:
        raise ValueError(f'invalid x value: {x}')
    result = 0.0 #Initialize as float
    eps_a = 1.0 
    tol = 1.0e-8 #Error tolerance (stopping criteria)
    k = 1 #Iteration variable
    fact_k = 1 #Initialize factorial 
    fact_2k = fact_k*2 #Initialize factorial 2k!
    k_max = 100
    #While loop
    while eps_a > tol and k < k_max:
        #dy = x**k/fact_k
        dy = ((2*x)**(2*k))/((k**2)*((fact_2k)/(fact_k**2)))
        result += dy
        eps_a = abs(dy/result)
        k += 1
        fact_k *= k 
        fact_2k *= (2*k)*((2*k)-1)
    return np.sqrt(0.5*result)





