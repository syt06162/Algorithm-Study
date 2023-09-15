import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))

INF = int(1e9)
distance = [INF for i in range(N+1)]

def dijkstra(v):
    Q = []
    distance[v] = 0
    heapq.heappush(Q, (0, v))
    while Q:
        dist, now = heapq.heappop(Q)
        if dist > distance[now] : # heapq 쓰기 때문!! 중요!!
            continue

        for next, cost in graph[now]:
            newCost = dist + cost
            if newCost < distance[next]:
                distance[next] = newCost
                heapq.heappush(Q, (newCost, next))

dijkstra(start)
print(distance)

'''

6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

'''