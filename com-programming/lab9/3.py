import numpy as np
M = np.array([[3, 2, 4], [5, 6, 2], [7, 1, 9]])
arr = []
for i in range(len(M[0])):
    if i == 0:
        m = M[:len(M), :1]
    else:
        m = M[:len(M), i]

    max_arr = max([int(x) for x in m])
    min_arr = min([int(x) for x in m])
    arr.append(max_arr-min_arr)

print(np.array(arr))
