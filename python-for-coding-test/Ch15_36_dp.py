# Ch15_36
# 핵심: MR 2차원

import sys
input = sys.stdin.readline

start = input().strip()
N = len(start)
dest = input().strip()
M = len(dest)

dp = [ [0 for i in range(M+1)] for j in range(N+1)]
for i in range(M+1):
    dp[0][i] = i
for i in range(N+1):
    dp[i][0] = i

for i in range(1,N+1):
    for j in range(1,M+1):
        if start[i-1] == dest[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

print(dp[N][M])

for i in range(N+1):
    print(*dp[i])