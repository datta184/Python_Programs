# iterating on 3-D array using ndenumerate
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

y=np.ndenumerate(arr)

for x in y:
    print(x)
        