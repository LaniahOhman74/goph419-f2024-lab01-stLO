'''
Inputs:
------------------------------------------------
Importing the launch angle range 
Creating a range of alpha values
Constant tol_alpha and ve_v0

Creating a range of ve_v0 values
constant tol_alpha and alpha

Results:
---------------------------------------------------
Plotting the alpha values against the launchangles generated
Plottin the ve_v0 values against the launchangles generated
In both cases generating two plots, one for the minimum launch angles and the other for the maximum launch angles generated

Notes:
--------------------------------------------------
Launch angles are inversely proportional to the altitude, meaning a small angle produces a large amplitude
'''
#Launch angle ranges for a constant ve_v0 but a range of alpha values
#Alpha values range from 0 to 0.32 with an increase of 0.01 
#imports
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp 

#import launch angle range definition 
from Launch_Angle_Range import launch_angle_range

def main():
    #Question Three
    ve_v0 = 2.0
    alpha = np.arange(0,0.33,0.01)
    tol_alpha = 0.04
    #minimum launch angle list
    min_la = []
    max_la = [] 
    for i in alpha:
        k = (launch_angle_range(ve_v0, i, tol_alpha))
        min_la.append(k[0])
        max_la.append(k[1])
    #print(min_la)
    #print(max_la)
    #Minumum launch angles for constant ve_v0 and tol_alpha but for ranges in alpha
    #Alpha is the altitude as a fraction of Earth's  radius
    plt.title('The launch angles versus Altitude')
    plt.plot(alpha,min_la, label = 'Minimum')
    plt.plot(alpha,max_la, label = 'Maximum')
    plt.xlabel('Altitude')
    plt.ylabel('Launch Angle')
    plt.legend()
    plt.savefig('Figures/ Altitude_Ranges')
    plt.show()

    #Question Four
    #Exact same thing but now for a range of ve_v0 
    ve_v0_range = np.arange(1.35,2.21,0.1)
    alpha = 0.25
    tol_alpha = 0.04
    #minimum launch angle list
    min_la1 = []
    max_la1 = [] 
    for i in ve_v0_range:
        k = (launch_angle_range(i, alpha, tol_alpha))
        min_la1.append(k[0])
        max_la1.append(k[1])
    #print(min_la1)
    #print(max_la1)
    #ve_v0 is the ratio of the escape velocity to the terminal velocity
    plt.title('The launch angles versus Velocity Ratio')
    plt.plot(ve_v0_range,min_la1, label = 'Mininum')
    plt.plot(ve_v0_range,max_la1, label = 'Maximum')
    plt.xlabel('Velocity Ratio')
    plt.ylabel('Launch Angle')
    plt.legend()
    plt.savefig('Figures/ Velocity_Ratio_Range')
    plt.show()

if __name__ == "__main__":
    main()

#Question Five 
#Errors
#Error in velocity ratio 
#Using sympy to compute the partial derivatives of equation 17
#Equation 17
#Defining the symbols 
ve_v0, alpha = sp.symbols('ve_v0 alpha')

Sinert = (1 + alpha)*sp.sqrt(1-((alpha/(1+alpha))*(ve_v0**2)))
#Partial derivative with ve_v0 being the variable and alpha being treated as a constant
p_ve_v0_Sinert = sp.diff(Sinert, ve_v0)
p_alpha_Sinert = sp.diff(Sinert, alpha)

#The error in Sinert(equation 17) in terms of error in ve_v0 and alpha
#Assigning values to varibles with the uncertanty in ve_v0 and alpha provided in question 5 
ve_v0_v = 2.0
alpha_v = 0.25 
delta_ve_v0 = 0.05
delta_alpha = 0.02

#First term df/dve_v0 * (delta_ve_v0)
f_term = (p_ve_v0_Sinert.subs({ve_v0: ve_v0_v, alpha: alpha_v}))*delta_ve_v0
print(f_term)
#Second term df/dalpha * (delta_alpha)
s_term = (p_alpha_Sinert.subs({ve_v0: ve_v0_v, alpha: alpha_v}))*delta_alpha
print(s_term)
#Total Error in Equation 17
Total_Error = f_term + s_term

print(Total_Error)