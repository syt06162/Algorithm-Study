# Ch12_11
# BOJ 3190

import sys
from collections import deque

N = int(input())
board = [[0 for j in range(N+2)] for i in range(N+2)]
# 1:사과 0:일반 9:벽 5:몸
for i in range(N+2):
    board[0][i] = 9
    board[N+1][i] = 9
    board[i][0] = 9
    board[i][N+1] = 9

K = int(input())
for i in range(K):
    y,x = map(int, sys.stdin.readline().split())
    board[y][x] = 1

turnQ = deque()
next = 0
L = int(input())
for i in range(L):
    time, dir = sys.stdin.readline().split()
    turnQ.append((int(time), dir))

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
dirIdx = 0

time = 0

cur_y, cur_x = 1,1
board[1][1] = 5
bodyQ = deque()
bodyQ.append((1,1))
while True:
    if next < len(turnQ) and turnQ[next][0] == time:
        time, dir = turnQ.popleft()
        if dir == 'L':
            dirIdx = (dirIdx+3)%4
        else:
            dirIdx = (dirIdx+1)%4
    time += 1

    new_y, new_x = cur_y + dy[dirIdx], cur_x + dx[dirIdx]
    
    if board[new_y][new_x] in [9, 5]:
        break
    elif board[new_y][new_x] == 1:
        board[new_y][new_x] = 5
        bodyQ.append((new_y, new_x))
    else: # 빈 공간
        board[new_y][new_x] = 5
        bodyQ.append((new_y, new_x))
        y, x = bodyQ.popleft()
        board[y][x] = 0
         
    cur_y, cur_x = new_y, new_x

print(time)


### print board
# for i in range(N+2):
#     for j in range(N+2):
#         print(board[i][j], end="")
#     print()
