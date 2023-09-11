# matrix rotation 90 degree

def rotate_90(old):
    N = len(old)
    new = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            new[j][N-1-i] = old[i][j]
    
    return new

# 90, 180, 270:
# https://shoark7.github.io/programming/algorithm/rotate-2d-array

# with zip (90)
import numpy as np

def zip_rotate(original):
    rotated = np.array(list(zip(*original[::-1])))
    return rotated