import numpy as np

#accessing 1D array element
arr = np.array([1,2,3,4])
# print(arr[0])

#accessing 2D array element
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('the 2nd element on 1st row: ', arr[0, 1])

#accessing 3D array element
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])

#negative indexing 
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('the last element from the second dim:' , arr[1, -2])

