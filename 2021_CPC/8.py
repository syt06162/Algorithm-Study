from collections import deque
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
# BFS

cutGraph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    cutGraph[a].append(b)
    cutGraph[b].append(a)
for i in range(N+1):
    cutGraph[i].sort()

visited = [False for i in range(N+1)]
distance = [INF for i in range(N+1)]

def bfs(start):
    Q = deque()
    visited[start] = True
    distance[start] = 0
    Q.append((0, start))

    while Q:
        dis, num = Q.popleft()
        cutList = cutGraph[num]
        cutLength = len(cutList)
        cutIdx = 0

        temp = []
        for i in range(1,N+1):
            if cutIdx != cutLength and i == cutList[cutIdx]:
                cutIdx += 1
                continue
            temp.append(i)
            if visited[i]==False:
                visited[i] = True
                distance[i] = dis+1
                Q.append((dis+1, i))
                
bfs(1) 
for i in range(1,N+1):
    print(distance[i])