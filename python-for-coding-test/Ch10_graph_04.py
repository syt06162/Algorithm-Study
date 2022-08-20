from collections import deque
import sys

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
time = [0 for i in range(N+1)]
indegree = [0 for i in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in temp[1:-1]:
        graph[j].append(i)
    time[i] = temp[0]
    indegree[i] = len(temp)-2

result = [i for i in time]

# print(graph)
# print(indegree)
Q = deque()
for i in range(1, N+1):
    if indegree[i]==0:
        Q.append(i)
while Q:
    now = Q.popleft()
    for node in graph[now]:
        indegree[node] -= 1
        # 핵심 수식
        result[node] = max(time[node] + result[now], result[node])
        if indegree[node] == 0:
            Q.append(node)
            

for i in range(1,N+1):
    print(result[i])