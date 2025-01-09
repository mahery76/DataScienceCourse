import numpy as np

#Slicing array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #[2, 3, 4, 5]
print(arr[4:]) #[5, 6, 7]
print(arr[:4]) #[1, 2, 3, 4]

#Negative slicing
print(arr[-3:-1]) #[5, 6]

#Step
print(arr[1:5:2])
print(arr[::2])
print(arr[1::2])

#Slicing 2D-array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[0:])
print(arr[1, 1:4]) #from the second element slice from index 1 to index 4 not included
print(arr[0:2, 2]) #from the first two elements, return index 2
print(arr[0:2, 1:4]) #from the first two elements, slice from index 1 to index 4 not included




