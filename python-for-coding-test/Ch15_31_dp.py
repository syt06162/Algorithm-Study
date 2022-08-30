# Ch15_30

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    nums = [ [] for i in range(N)]
    for i in range(N):
        for j in range(M):
            nums[i].append(temp[i*M+j])

    dp = [ [0 for i in range(M)] for i in range(N)]
    for i in range(N):
        dp[i][0] = nums[i][0]

    for j in range(1, M):
        for i in range(0, N):
            if N==1:
                dp[i][j] = dp[0][j] + nums[i][j]
            elif N==2:
                dp[i][j] = max(dp[0][j-1], dp[1][j-1]) + nums[i][j]
            else:
                if i==0:
                    dp[i][j] = max(dp[1][j-1], dp[0][j-1]) + nums[i][j]
                elif i == N-1:
                    dp[i][j] = max(dp[N-1][j-1], dp[N-2][j-1]) + nums[i][j]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1], dp[i+1][j-1]) + nums[i][j]

    # max 구하기
    result = 0
    for i in range(N):
        result = max(result, dp[i][M-1])
    print(result)
