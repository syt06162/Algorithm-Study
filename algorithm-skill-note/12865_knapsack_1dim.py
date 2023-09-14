import sys
input = sys.stdin.readline

# 1차원 knap
N, K = map(int, input().split())
lst = []
for i in range(N):
    W, V = map(int, input().split())
    lst.append((W, V))

dp = [-1 for i in range(K+1)]
dp[0] = 0
for w, v in lst: # 매번 갱신
    for i in range(K, -1, -1): # 꼭 뒤부터! 앞부터하면 중복가능
        if i-w < 0 or dp[i-w]==-1:
            continue
        dp[i] = max(dp[i], dp[i-w]+v)
print(max(dp))

# print(dp)