#Launch angle ranges for a constant ve_v0 but a range of alpha values
#Alpha values range from 0 to 0.32 with an increase of 0.01 
#imports
import matplotlib.pyplot as plt
import numpy as np
#import launch angle range definition 
from Launch_Angle_Range import launch_angle_range
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
print(min_la)
print(max_la)
#Minumum launch angles for constant ve_v0 and tol_alpha but for ranges in alpha
plt.plot(alpha,min_la)
plt.plot(alpha,max_la)
plt.show()
if __name__ == "main":
    main()