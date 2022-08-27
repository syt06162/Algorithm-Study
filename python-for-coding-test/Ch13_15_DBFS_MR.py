# Ch13_15
# boj 18352
# 핵심: bfs with DISTANCE

from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().split())

# 그래프 입력
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [False for i in range(N+1)]

def bfs(start):
    Q = deque()

    distance = 0
    visited[start] = True
    Q.append((start, distance))

    result = []
    while Q:
        now, distance = Q.popleft()
        for node in graph[now]:
            if visited[node] == False:
                visited[node] = True
                Q.append((node, distance+1))
                if distance+1 == K:
                    result.append(node)
    result.sort()
    return result

# bfs 처리
result = bfs(X)
if len(result) == 0:
    print(-1)
else: 
    for i in range(len(result)):
        print(result[i])
    