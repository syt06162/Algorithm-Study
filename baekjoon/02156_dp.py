import sys

N = int(input())
lst = []
for i in range(N):
  lst.append(int(sys.stdin.readline()))

dp = [0]*N #lst[i] 를 꼭 마신다고 가정했을 때 최대값
dp[0] = lst[0]
if N>=2:
  dp[1] = lst[0] + lst[1]
if N>=3:
  dp[2] = max(lst[0]+lst[2], lst[1]+lst[2], lst[0]+lst[1]) 
for i in range(3,N):
  dp[i] = max(dp[i-3]+lst[i-1]+lst[i], dp[i-2]+lst[i], dp[i-1])

print(max(dp))
print(dp)