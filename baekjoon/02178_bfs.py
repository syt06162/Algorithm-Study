import sys
from collections import deque

di = [-1,0,1,0]
dj = [0,1,0,-1]

def bfs(graph, start_I, start_J, dest_I, dest_J):
    Q = deque()
    graph[start_I][start_J] = 0
    count = 1
    Q.append((start_I, start_J, count))

    while Q:
        i, j, count = Q.popleft()
        if i==dest_I and j==dest_J:
            break

        for k in range(4):
            ni = i+di[k]   
            nj = j+dj[k]
            if ni<0 or ni>dest_I or nj<0 or nj>dest_J or graph[ni][nj]==0:
                continue
            Q.append((ni,nj,count+1))
            graph[ni][nj] = 0

    return count

size_I, size_J = map(int, sys.stdin.readline().split())
graph = []
for i in range(size_I):
    graph.append(list(map(int, sys.stdin.readline().strip())))

for i in range(size_I):
    print(graph[i])

#print(bfs(graph, 0, 0, size_I-1, size_J-1))