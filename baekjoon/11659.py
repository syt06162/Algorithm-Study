import sys

input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

hap = [0] #부분합
sums = 0
for i in range(N):
    sums += nums[i]
    hap.append(sums)
    
# 결과
for i in range(M):
    l, r = map(int, input().split())
    print(hap[r] - hap[l-1])