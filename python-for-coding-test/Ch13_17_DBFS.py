# Ch13_17
# boj 18405
# 핵심: bfs

import sys

# 입력받기
N, K = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
S, Y, X = map(int, sys.stdin.readline().split())

#bfs 구현
import heapq
def bfs(time):
    Q = []
    # board 바이러스 시작점들 입력
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                heapq.heappush(Q, (board[i][j], i,j))
    
    second = 0
    dy = [-1,1,0,0] # 상하좌우
    dx = [0,0,-1,1]

    while second < time:
        nextQ = []
        while Q:
            val, y, x = heapq.heappop(Q)
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny<0 or ny>=N or nx<0 or nx>=N:
                    continue

                # 0 에만 바이러스 퍼뜨리고 큐에 넣기
                if board[ny][nx] == 0:
                    board[ny][nx] = val
                    nextQ.append((val, ny,nx))

        for temp in nextQ:
            heapq.heappush(Q, temp)
        second += 1

bfs(S)
print(board[Y-1][X-1])

