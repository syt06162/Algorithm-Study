import sys

N, M = map(int, sys.stdin.readline().split())
Y, X, dir = map(int, sys.stdin.readline().split())

###### 문제에서, 방문한 칸의 수 라는 것을 중복은 제외함. 즉, 이미 가본 좌표를 다시 방문하여도 1번으로 침

# 맵을 담을 리스트
# 0은 (안가본)길, 1은 바다, 2는 길인데 이동한 길
lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

moveCount = 1
lst[Y][X] = 2

while True:
    goFlag = False # 이동을 했는지 기록하는 flag
    
    for i in range(4):
        dir = (dir - 1)%4
        ny = Y + dy[dir]
        nx = X + dx[dir]

        if lst[ny][nx] == 0:
            # 아직 안 가본 갈수 있는 곳이니 이동!
            Y = ny
            X = nx
            goFlag = True
            lst[Y][X] = 2
            moveCount += 1
            break
    
    # 이동을 한 경우 : 다시 반복문을 돈다
    if goFlag == True:
        continue
    # 이동을 4 방향 모두 못하니까, 뒤로 간다.
    else: 
        ny = Y + dy[(dir+2)%4]
        nx = X + dx[(dir+2)%4]
        # 뒤로 갈 곳이 바다면 stop
        if lst[ny][nx] == 1:
            break
        else:
            Y = ny
            X = nx

print(moveCount)

# debug - map print
for i in range(N):
    for j in range(M):
        print(lst[i][j], end=" ")
    print()
