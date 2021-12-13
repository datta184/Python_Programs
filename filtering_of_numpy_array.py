'''
FILTERING ARRAY

Getting some elements out of an existing array and creating a new array out of them is called filtering.

NumPy filter an array using a boolean index list.

A boolean index list is a list of booleans corresponding to indexes in the array.


'''
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])
filter = [True,False,True,False,True,False,True,False,True]

fil=arr[filter]

print("the initial array is :",arr)
print("the filtered array is:",fil)