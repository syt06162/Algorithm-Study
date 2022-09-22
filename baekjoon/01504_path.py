import heapq
import sys
input = sys.stdin.readline

# 1 a b N 
# 1 b a N 중 최소값

N, E = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))
ma, mb = map(int, input().split())

def dijkstra(start, ma, mb):
    INF = int(1e9)

    # 1a, 1b 구하기
    Q = []
    distance = [INF for i in range(N+1)]
    distance[start] = 0
    heapq.heappush(Q, (0, start))
    while Q:
        dist, now = heapq.heappop(Q)
        if dist > distance[now] :
            continue

        for next, cost in graph[now]:
            newCost = dist + cost
            if distance[next] > newCost:
                distance[next] = newCost
                heapq.heappush(Q, (newCost, next))
    return (distance[ma], distance[mb])

_1a, _1b = dijkstra(1,ma,mb)
_an, _bn = dijkstra(N,ma,mb)
_ab, temp = dijkstra(ma,mb,1)

INF = int(1e9)
minVal = INF
for val in (_1a + _ab + _bn, _1b + _ab + _an):
    minVal = min(val, minVal)

if minVal == INF:
    print(-1)
else:
    print(minVal)