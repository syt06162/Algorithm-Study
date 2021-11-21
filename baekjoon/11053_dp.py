import sys

N = int(input())
lst = list(map(int,sys.stdin.readline().split()))

dp = [[lst[i],1] for i in range(N)]  # val,streak

for i in range(1, N):
    val = lst[i] 

    for j in range(0,i):
        if dp[j][0] < val:
            dp[i] = max([val, dp[j][1]+1], dp[i], key = lambda x: x[1])

val, streak = max(dp, key=lambda x: x[1])
print(streak)
