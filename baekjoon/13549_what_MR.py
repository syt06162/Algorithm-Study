from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INF = 100000
visited = [-1 for i in range(INF + 1)]

Q = deque()
visited[N] = 0
Q.append(N)
while Q:
    num = Q.popleft()
    second = visited[num]
    if num==K:
        print(second)
        break

    for next in (num-1, num+1, 2*num):
        if next<0 or next>INF or visited[next] != -1: continue

        if next == 2*num:
            visited[next] = second
            Q.appendleft(next)
        else:
            visited[next] = second + 1
            Q.append(next)
