# spliting array
import numpy as np

arr =np.array([1,2,3,4,5,6,7,8,9])

new_arr = np.split(arr,3)

print(new_arr)

for i in new_arr:
    print(i)