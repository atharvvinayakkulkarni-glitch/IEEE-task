import numpy as np
# 5*5 array of random integers between 0 and 100
arr=np.random.randint(1,100,(5,5))
# normalise between 0 and 1
norm_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
# slice to get 3*3 array 
sliced = arr[1:4, 1:4]
print('sliced array:', sliced)
# dot product of first and last row
print('dot product of first and last row:', np.dot(sliced[0, : ], sliced[2, : ]))
