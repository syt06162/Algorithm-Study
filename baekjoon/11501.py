N, K = map(int, input().split())

if N-K < K:
    K = N-K

dp = [[1]*i for i in range(1, N+2) ]

for i in range(2, N+1):
    for j in range(1, i):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%10007

# if a = b+c
# then a mod r = (b+c) mod r
print(dp[N][K])