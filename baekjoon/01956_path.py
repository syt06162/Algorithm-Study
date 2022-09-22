import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = int(1e9)
graph = [[INF for i in range(V+1)] for j in range(V+1)]
for i in range(E):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost

# 플로이드
for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j] = min(graph[i][k]+graph[k][j] , graph[i][j])

# 사이클 
minCycle = INF
for i in range(1,V+1):
    minCycle = min(minCycle, graph[i][i])

if minCycle == INF:
    print(-1)
else:
    print(minCycle)