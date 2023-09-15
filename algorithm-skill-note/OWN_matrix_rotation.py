# matrix rotation 90 degree

def rotate_90(old):
    N = len(old)
    new = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(N):
            new[j][N-1-i] = old[i][j]
    
    return new

# easy
original = [[1, 2], [3, 4], [5, 6]]
rotated = list(zip(*original[::-1]))

for i in range(len(original)):
    print(*original[i])
print()    
for i in range(len(rotated)):
    print(*rotated[i])