import numpy as np

arr_1d=np.array([1,2,3,4,5])
arr_2d=np.array([[1,2,3],[4,5,6]])  
arr_3d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(arr_1d.ndim)  # 1
print(arr_2d.ndim)  # 2
print(arr_3d.ndim)  # 3

# ndim is used to find the dimension of the array