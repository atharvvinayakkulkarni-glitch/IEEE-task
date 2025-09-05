import numpy as np
arr=np.random.randint(1,100,(5,5))
for row in arr:
    for x in row:
        print(x, end=" ")
    print('')
print('MAX:', np.max(arr))
print('MIN:', np.min(arr))
print('MEAN:', np.mean(arr))
norm_arr = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
print('normalized array:', norm_arr)
flat = norm_arr.flatten()
print('Flattened normalised array:', np.sort(flat))
