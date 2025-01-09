import numpy as np

# checking version
# print(np.__version__)


# create an ndarray
arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))


# Dimensions array
# 0-D arrays
arr = np.array(42)
# print(arr)

# 1-D arrays
arr = np.array([1,2,3,4,5])
# print(arr)

# 2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# 2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)

# 3-D arrays 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr)
# print(arr.ndim)


arr = np.array([1,2,3,4], ndmin = 5)
print(arr)
print('number of dimension: ', arr.ndim)