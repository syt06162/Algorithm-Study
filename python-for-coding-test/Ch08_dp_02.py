import sys

# 바텀업 방식으로 풀기

N = int(input())

dp = [0 for i in range(N+1)]

for i in range(2,N+1):
    # 1 빼기
    dp[i] = min(dp[i], dp[i-1] + 1)
    # 2나누기
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3나누기
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 5나누기
    if i%5==0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[N])