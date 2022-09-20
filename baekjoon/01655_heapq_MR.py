import sys
import heapq

input = sys.stdin.readline
N = int(input())

nowMid = int(input())
lQ = [] # 최대힙으로 사용
lcount = 0
rQ = []
rcount = 0
print(nowMid)

for i in range(N-1):
    val = int(input())
    if val < nowMid:
        if lcount == rcount:
            heapq.heappush(rQ, nowMid)
            heapq.heappush(lQ, -val)
            nowMid = -heapq.heappop(lQ)
            rcount += 1
        else:
            heapq.heappush(lQ, -val)
            lcount += 1
    else:
        if lcount == rcount:
            heapq.heappush(lQ, -nowMid)
            heapq.heappush(rQ, val)
            nowMid = -heapq.heappop(lQ)
            rcount += 1
        else:
            heapq.heappush(lQ, -nowMid)
            heapq.heappush(rQ, val)
            nowMid = heapq.heappop(rQ)
            lcount += 1
    print(nowMid)
