# Ch16_34
# boj 18353

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.reverse()

dp = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))