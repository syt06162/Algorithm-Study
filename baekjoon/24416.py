import sys
input = sys.stdin.readline

N = int(input())
dp = [-1 for i in range(N+1)]
def fibo(n):
    dp[1] = dp[2] = 1
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

print(fibo(N), N-2)