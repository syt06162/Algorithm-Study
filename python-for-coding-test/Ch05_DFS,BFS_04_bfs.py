import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [[] for i in range(N)]
for i in range(N):
    st = sys.stdin.readline()
    for j in range(M):
        maze[i].append(int(st[j]))

# 초기 좌표
Y, X = 0, 0

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# def printmap():
#     for i in range(N):
#         for j in range(M):
#             print(maze[i][j], end="")
#         print()

def bfs(Y, X):
    Q = deque()
    # y,x, step
    step = 1
    Q.append((Y,X,step))

    finishFlag = False
    while Q:
        # print()
        # printmap()
        y,x, step = Q.popleft()
        step += 1
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            # 종료지점
            if ny==N-1 and nx==M-1:
                finishFlag = True
                break
            # 범위아니거나, 벽이거나, step높거나
            elif ny<0 or ny>=N or nx<0 or nx>=M or maze[ny][nx]!=1:
                continue
            else:
                maze[ny][nx] = step
                Q.append((ny, nx, step))

        if finishFlag == True:
            break
    
    if finishFlag == True:
        print(step)
    else:
        print("cannot go to exit")

bfs(Y,X)
