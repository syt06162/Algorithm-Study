# Ch15_33
# boj 14502

import sys
input = sys.stdin.readline

N = int(input())
endDate = [ [] for i in range(N+2)] # end 에 (start, price)
for i in range(1, N+1):
    term, price = map(int, input().split())
    endDay = i + term
    if endDay <= N+1:
        endDate[endDay].append((i, price))


dp = [0 for i in range(N+2)]
for day in range(1, N+2):
    dp[day] = dp[day-1] # 놓치기 쉬운 오류!
    for start, price in endDate[day]:
        dp[day] = max(dp[day], dp[start] + price)
print(max(dp))