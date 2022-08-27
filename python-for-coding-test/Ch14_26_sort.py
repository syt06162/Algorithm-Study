# Ch13_26
# boj 1715
# 핵심: 매순간 작은수2개 합치고 정렬. 이때 정렬 위해 heapq

import sys
import heapq

N = int(input())
Q = []
for i in range(N):
    heapq.heappush(Q, int(sys.stdin.readline())) 

left = N
result = 0
while left > 1:
    min1 = heapq.heappop(Q)
    min2 = heapq.heappop(Q)
    
    hap = min1 + min2
    result += hap
    heapq.heappush(Q, hap)

    left -= 1


print(result)