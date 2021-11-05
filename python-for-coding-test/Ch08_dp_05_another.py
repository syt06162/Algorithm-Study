import sys

N, M = map(int, sys.stdin.readline().split())
dp = [0] * (M+1)
coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline()))

for num in range(1,M+1):
    tempList = []
    for coin in coins:
        if num-coin>=0 and dp[num-coin] != -1:
            tempList.append(dp[num-coin] + 1)

    if tempList:
        dp[num] = min(tempList)
    else:
        dp[num] = -1

# for i in range(1,M+1):
#     print("%2d" % (i), dp[i] )
print(dp[M])
# 시간복잡도 : O(N*M)