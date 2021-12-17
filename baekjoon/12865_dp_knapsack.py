import sys

# 냅색 알고리즘 
# 힌트 참고함

N, K = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split()))) # W, V

dp = [[0 for i in range(K+1)] for j in range(N)]
for j in range(lst[0][0], K+1):    
    dp[0][j] = lst[0][1]

for i in range(1, N):
    for j in range(0, K+1):
        if j < lst[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-lst[i][0]] + lst[i][1])

print(dp[N-1][K])