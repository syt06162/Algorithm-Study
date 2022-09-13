# Ch17_38
# 핵심: 플로이드 워셜을 쓴다는 사실

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

INF = int(1e9)
dis = [[INF for i in range(N+1)] for i in range(N+1)]
for i in range(1, N+1):
    dis[i][i] = 0
for i in range(M):
    a, b = map(int, input().split())
    dis[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

result = 0
for i in range(1, N+1):
    count = 0
    for j in range(1,N+1):
        if dis[i][j] != INF or dis[j][i] != INF:
            count += 1
    if count == N:
        result += 1
print(result)