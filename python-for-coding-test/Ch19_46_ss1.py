from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))


# 시작위치
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            startY = i
            startX = j
            break
size = 2
nowEat = 0

#bfs 시작
dy = [-1,0,1,0] #상 좌 하 우
dx = [0,-1,0,1]
visited = [[False for i in range(N)] for j in range(N)]

Q = deque()
Q.append((0, startY, startX))
visited[startY][startX] = True
board[startY][startX] = 0

result = 0
candi = []
candi_D = -1
while Q:
    d, y, x = Q.popleft()
    d += 1
    if not candi or candi_D == d:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny<0 or ny>=N or nx<0 or nx>=N or size<board[ny][nx] or visited[ny][nx]==True:
                continue
            
            # 이동
            if board[ny][nx]==0 or board[ny][nx]==size:
                Q.append((d, ny, nx))
                visited[ny][nx] = True
            # 먹기 - 후보들 비교
            elif size > board[ny][nx]:
                visited[ny][nx] = True
                candi_D = d
                candi.append((ny,nx))
    
    # 후보중 먹기
    if not Q and candi:
        candi.sort()
        ny = candi[0][0]
        nx = candi[0][1]
        
        result += candi_D
        nowEat += 1
        if nowEat == size:
            size += 1
            nowEat = 0
        
        Q = deque()
        Q.append((0,ny,nx))
        visited = [[False for i in range(N)] for j in range(N)]
        visited[ny][nx] = True
        board[ny][nx] = 0
        candi = []
        candi_D = -1
            
print(result)
            