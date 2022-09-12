# Ch15_40
# 

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#다익스트라
INF = int(1e9)
distance = [INF for i in range(N+1)]
Q = []
distance[1] = 0
heapq.heappush(Q, (0, 1))
while Q:
    dis, now = heapq.heappop(Q)
    if dis > distance[now]:
        continue

    for new in graph[now]:
        cost = dis + 1
        if cost < distance[new]:
            distance[new] = cost
            heapq.heappush(Q, (cost, new))

# 최대값과 개수찾기
maxVal = -1
maxIdx = -1
maxCount = 0
for i in range(1, N+1):
    if distance[i] > maxVal:
        maxCount = 1
        maxIdx = i
        maxVal = distance[i]
    elif distance[i] == maxVal:
        maxCount += 1
print(maxIdx, maxVal, maxCount)