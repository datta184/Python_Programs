'''
Joining Arrays Using Stack Functions

Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

'''
import numpy as np

array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])

z = np.stack((array_1,array_2)) # bydefault axixs is 0 
y = np.stack((array_1,array_2),axis = 1)
print("\nbydefault:\n",z)
print("\nwith axis = 1 :\n",y)