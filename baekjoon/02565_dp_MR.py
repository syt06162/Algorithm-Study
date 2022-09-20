import sys
input = sys.stdin.readline

N = int(input())
lines = []
for i in range(N):
    lines.append(list(map(int, input().split())))

lines.sort(key = lambda x: x[1])

dp = [1 for i in range(N)]
for i in range(1,N):
    for j in range(0,i):
        if lines[j][0] < lines[i][0] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1

print(N - max(dp))