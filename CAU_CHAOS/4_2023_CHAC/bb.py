import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())
ppM = M
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

from collections import deque
def bfs(y,x):
    can = 0
    Q = deque()

    board[y][x] = 1
    can += 1
    Q.append((y,x))
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    while Q:
        y,x = Q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny<0 or nx<0 or ny>=N or nx>= N or board[ny][nx]==1:
                continue
            board[ny][nx] = 1
            can += 1
            Q.append((ny,nx))
    return can

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            can = bfs(i,j)
            poja = can//K
            if can%K != 0:
                poja += 1
            M -= poja
            if M <0:
                print("IMPOSSIBLE")
                exit()

if M==ppM:
    print("IMPOSSIBLE")
    exit()
print("POSSIBLE")
print(M)