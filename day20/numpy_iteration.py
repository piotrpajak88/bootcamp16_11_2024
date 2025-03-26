import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)

for x in arr:
    print(x)
    for y in x:
        print(y)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print(arr)

# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

for x in np.nditer(arr):
    print(x)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# np.bytes_(b'1')
# np.bytes_(b'2')
# np.bytes_(b'3')

arr = np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(arr[:,::2]):
    print(x)

# 1
# 3
# 5
# 7

