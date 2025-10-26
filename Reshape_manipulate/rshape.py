import numpy as np

arr=np.array ([2,3,4,5])
reshape_arr=arr.reshape (2,2)
print(reshape_arr)  #!d [[2 3 4 5]]

#it does not create copy of original array, it just changes the shape of original array
# 1d to multi d