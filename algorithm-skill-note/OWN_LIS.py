import sys
input = sys.stdin.readline
# boj 11053

N = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(N)] # streak
for i in range(1,N):
    for j in range(0,i):
        if lst[j] < lst[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
print(max(dp))
