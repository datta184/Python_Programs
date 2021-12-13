
from numpy import *

arr = array([])

n=int(input("enter number of values that you want to insert: "))

for i in range(n):
    v=input("enter the element: ")
    arr = append(arr,v)
print("the array is:",arr)
print(type(arr))
