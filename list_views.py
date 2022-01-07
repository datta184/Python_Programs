# copy presers the orignal list bu t view not preserve orignal list

import numpy as np
x=np.array([1,2,3,4,5,6,7])
y=x.view()

print("\n",x)
print("\n",y)

x[0]=100


print("**********************************************************")


print("\n",x)
print("\n",y)