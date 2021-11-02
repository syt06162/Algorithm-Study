import sys
from collections import deque

def bfs(graph, start, visited):
    Q = deque()
    visited[start] = 0
    Q.append((start, 0))

    while Q:
        val, num = Q.popleft()
        nextNum = (num+1)%2 #0이면 1로, 1이면 0으로

        for i in graph[val]:
            if visited[i]==-1: #방문하지 않은 곳이면 
                visited[i] = nextNum #반대 분류에 넣어준다
                Q.append((i, nextNum))
            elif visited[i] == num: #인접한 곳에 같은 분류라면 False
                return False

    return True # 다 돌았는데 문제없으면 True


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
    # BFS를 돌며 아직 방문하지 않은 노드들을 분류함.
    # 우선 0배열로 분류하고, 그 인접한 노드들은 1번 노드로 분류, 그 인접한 노드들은 다시 0번으로 분류.
    # 이런식으로 분류하다가 겹치는거 (아까 0번지로 이미 분류했는데 1번지로 또 분류해야하는 상황 등) 생기면 NO 출력
    for i in range(1,V+1):
        flag = True
        if visited[i] == -1:
            flag = bfs(graph, i, visited)
            if flag==False:
                print("NO")
                break
    else: print("YES")
    