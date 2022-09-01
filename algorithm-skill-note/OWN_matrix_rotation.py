# matrix rotation 90 degree

def rotate_90(old):
    N = len(old)
    new = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            new[j][N-1-i] = old[i][j]
    
    return new