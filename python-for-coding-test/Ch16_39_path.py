# Ch15_39
# 시뮬레이션 + 다익스트라

import heapq
import sys
input = sys.stdin.readline
dy = [-1,1,0,0]
dx = [0,0,-1,1]
INF = int(1e9)

T = int(input())
for _ in range(T):

    N = int(input())
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    
    distance = [[INF for i in range(N)] for j in range(N)]
    distance[0][0] = board[0][0]
    Q = []
    heapq.heappush(Q, (distance[0][0], (0,0)))
    while Q:
        dis, (nowY, nowX) = heapq.heappop(Q)
        if dis > distance[nowY][nowX]:
            continue

        for k in range(4):
            newY = nowY + dy[k]
            newX = nowX + dx[k]
            if newY < 0 or newY >= N or newX < 0 or newX >= N:
                continue

            cost = dis + board[newY][newX]
            if cost < distance[newY][newX]:
                distance[newY][newX] = cost
                heapq.heappush(Q, (cost, (newY, newX)))
    print(distance[N-1][N-1])
                
