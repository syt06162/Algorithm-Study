def solution(tri):
    N = len(tri)
    for i in range(1,N):
        for j in range(0,i+1):
            if j== 0:
                tri[i][j] += tri[i-1][j]
            elif j==i:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
    
    return max(tri[N-1])