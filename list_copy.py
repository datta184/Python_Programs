import numpy as np
a = np.array([1,2,3,4,5,6])
x = a.copy()

print("\na = ",a)
print("*******************************************")
print("\nx = a.copy()")
print("\n*******************************************")
print("\nx = ",x)

print("*******************************************")
print("\nx[0]=100")
print("\n*******************************************")

x[0]=100

print("\na = ",a)

print("\nx = ",x)

print("\na = ",a)