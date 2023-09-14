import sys
input = sys.stdin.readline

# 2차원 knap
MAXI = 100
dp = [ [-1 for i in range(MAXI+1)] for j in range(MAXI+1)]
N, M = map(int, input().split())

lst = []
for i in range(M):
    r,b, cost = map(int, input().split())
    lst.append([r,b,cost])

dp[0][0] = 0

# lst 하나씩 추가
for r,b, cost in lst:
    for i in range(MAXI, -1 ,-1 ): 
        for j in range(MAXI, -1 ,-1 ):             
            nowR = i-r
            nowB = j-b
            if nowR <0 or nowB <0 or dp[nowR][nowB] == -1:
                continue
            if dp[i][j] < dp[nowR][nowB] + cost:
                dp[i][j] = dp[nowR][nowB] + cost
       

results = []
for i in range(N):
    r,b = map(int, input().split())
    if dp[r][b] == -1:
        results.append([i+1, 0])
    else:
        results.append([i+1, dp[r][b]])
results.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
    print(*results[i])
