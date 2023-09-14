import sys
input = sys.stdin.readline

M, S = map(int, input().split(":"))
time = M*60 + S
time //= 10

# 1,6,60,3s
dp = [ int(1e9) for i in range(max(3+1, time+1))]
dp[0] = 1 #?
dp[1] = 2
dp[2] = 3
dp[3] = 1

if time <= 3:
    print(dp[time])
    exit()

lst = [1,6,60,3]
for i in range(3, time+1):
    for j in lst:
        if i-j>=0:
            dp[i] = min(dp[i], dp[i-j] + 1)

print(dp[time])