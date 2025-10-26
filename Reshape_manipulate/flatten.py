"""

.ravel() - function to flatten an array ->view of original array
.flatten() - function to flatten an array ->copy of original array
"""
import numpy as np
arr=np.array ([[1,2,3],[4,5,6]])
print(arr.ravel())   #!d [1 2 3 4 5 6]   #view of original array
print(arr.flatten()) #!d [1 2 3 4 5 6]   #copy of original array