import numpy as np
# 5*5 array of random integers from 0 to 100
arr=np.random.randint(1,100,(5,5))
# printing in grid format
for row in arr:
    for x in row:
        print(x, end=" ")
    print('')
# printing max,min and mean
print('MAX:', np.max(arr))
print('MIN:', np.min(arr))
print('MEAN:', np.mean(arr))
# normalised array with values between 0 and 1
norm_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print('normalized array:', norm_arr)
# flatten into linear array of size 25
flat = norm_arr.flatten()
print('Flattened normalised array:', np.sort(flat))
