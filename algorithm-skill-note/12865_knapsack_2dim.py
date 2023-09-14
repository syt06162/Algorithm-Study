import sys

N , K = map(int, sys.stdin.readline().split())

# 2차원 냅색
dp = [ [0 for i in range(K+1)] for j in range(N+1)]
knap = [[]]
for i in range(N):
    w, v = map(int, sys.stdin.readline().split())
    knap.append([w,v])

for i in range(1, N+1):
    w, v = knap[i]
    for j in range(1, K+1):
        if j< w:
            dp[i][j] = dp[i-1][j] # 이번거 못담으면, 기존과 동일
        else:
            dp[i][j] = max( dp[i-1][j], v + dp[i-1][j-w]) # 담을 수 있으면 비교후 담아

print(dp[N][K])
# for i in range(1,N+1):
#     print(dp[i])