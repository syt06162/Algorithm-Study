import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split())
indegree = [ 0 for i in range(v+1)]
graph = [ [] for i in range(v+1) ]

for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상정렬: indegree 0을, deque로.
def topology_sort():
    q = deque()
    result = []

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for ver in graph[now]:
            indegree[ver] -= 1
            if indegree[ver] == 0 :
                q.append(ver)
    
    return result

print(*topology_sort())


'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''