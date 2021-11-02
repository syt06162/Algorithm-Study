import sys
from collections import deque

def bfs(graph, start, visited):
    Q = deque()
    visited[start] = 0
    Q.append((start, 0))

    while Q:
        val, num = Q.popleft()
        print("--",val, num )
        nextNum = (num+1)%2 #0이면 1로, 1이면 0으로

        for i in graph[val]:
            if visited[i]==-1:
                visited[i] = nextNum
                Q.append((i, nextNum))
            elif visited[i] == num:
                return False

    return True



T = int(input())
for _case in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = dict()
    for i in range(1,V+1):
        graph[i] = []
    for i in range(E):
        u,v = map(int,sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [-1 for i in range(V+1)] #0번지는 사용하지 않음 # -1:방문하지 않음, 0:0번분류, 1:1번분류
    for i in range(1,V+1):
        flag = True
        if visited[i] == -1:
            flag = bfs(graph, i, visited)
            if flag==False:
                print("NO")
                break
    else: print("YES")
    