import sys

N = int(input())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))

if N<=3:
    if N==1:
        print(lst[0])
    elif N==2:
        print(lst[0]+lst[1])
    elif N==3:
        print(max(lst[0]+lst[2], lst[1]+lst[2]))
    exit(0)

dp = [-1]*N
dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[0]+lst[2],lst[1]+lst[2])
for i in range(3, N):
    dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i])

print(dp[N-1])