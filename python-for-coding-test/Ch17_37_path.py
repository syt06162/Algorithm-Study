# Ch17_37
# boj 11404
# 플로이드

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# path 배열
INF = int(1e9)
path = [[INF for i in range(N+1)] for j in range(N+1)]
for i in range(1,N+1):
    path[i][i] = 0

# 경로 입력
for i in range(M):
    a,b,c = map(int, input().split())
    path[a][b] = min(path[a][b], c)

# 플로이드 워셜
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            path[i][j] = min(path[i][j], path[i][k] + path[k][j])

# 출력
for i in range(1,N+1):
    for j in range(1,N+1):
        if path[i][j] == INF:
            path[i][j] = 0

for i in range(1,N+1):
    print(*path[i][1:])

