import numpy as np

"""
array[start:end:step] #!d slice of the array

arr[start:end] #start to end-1
negative step,-1 means reverse
"""

arr=np.array ([10,20,30,40,50,60,70,80,90])

print(arr[2:7:2])    #!d [30 50 70]
print(arr[5:])       #!d [60 70 80 90]
print(arr[:4])       #!d [10 20 30 40]
print(arr[::-1])     #!d [90 80 70 60 50 40 30 20 10]