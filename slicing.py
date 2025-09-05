import numpy as np
arr=np.random.randint(1,100,(5,5))
norm_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
sliced = arr[1:4, 1:4]
print('sliced array:', sliced)
print('dot product of first and last row:', np.dot(sliced[0, : ], sliced[2, : ]))
