from collections import deque
import sys
input = sys.stdin.readline

# bfs 쓰기
# 1에서 2,3,4,5,6,7 연결
N, M = map(int, input().split())

graph = [ [] for i in range(101)] #0번지 x
special = [ -1 for i in range(0,101)]
for i in range(N+M):
    a, b = map(int, input().split())
    special[a] = b

# 그래프 잇기
for i in range(1,101):
    upper = min(i+7, 101)
    for j in range(i+1, upper):
        if special[j] == -1:
            graph[i].append(j)
        else:
            graph[i].append(special[j])

# bfs 시작
def dfs():
    visited = [False for i in range(0,101)]
    Q = deque()
    Q.append((0, 1)) # len, x
    visited[1] = True

    while Q:
        length, now = Q.popleft()
        for next in graph[now]:
            if next == 100:
                return length + 1
            if not visited[next]:
                visited[next] = True
                Q.append((length + 1, next))

print(dfs())


