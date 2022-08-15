import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)


# 개선된 다익스트라 알고리즘. 
# get_smallest_node 를 사용하지 않고, heapq에 넣는다. O(E logV)

def dijkstra(start): 
    distance[start] = 0    
    q = []
    heapq.heappush(q, (0, start))

    while q:
        nowCost, nowVer = heapq.heappop(q)
        print(q)
        if distance[nowVer] < nowCost: 
            # 밑에 (if distance[j[0]] > cost) 일때만 push 되는데 저게 더 작은거 는 어떻게 들어왔지? 
            # 우선순위큐이기 때문에 cost가 더 큰값이 먼저 들어왔다가 더 나중에 나감
            continue

        for j in graph[nowVer]:
            cost = nowCost + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

V, E = map(int, input().split())
start = int(input())
graph = [ [] for i in range(V+1) ]
distance = [INF for i in range(V+1) ]

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

dijkstra(start)

for i in range(1, V+1):
    print(i, ": ", end="")
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2