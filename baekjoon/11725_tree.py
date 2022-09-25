import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

N = int(input())
parent = [-1 for i in range(N+1)] #0 사용x
parent[1] = 1
# 우선 부모든 자식이든 graph에 다 연결,
# dfs 도는데, 돌때 부모는 제외하고 돈다

graph = [[] for i in range(N+1)] #0샤용x
for i in range(N-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now, par):
    parent[now] = par
    for child in graph[now]:
        if child == par:
            continue
        dfs(child, now)

dfs(1, -1)
    
for i in range(2,N+1):
    print(parent[i])