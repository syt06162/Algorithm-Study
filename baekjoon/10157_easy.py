C, R = map(int, input().split())
N = int(input())

if N > C*R:
    print(0)
else:
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    board = [ [0 for i in range(C)] for j in range(R)]
    # 시작
    x = 0
    y = 0
    dir = 0 # 0 1 2 3 # 상 우 하 좌
    
    cnt = 1
    while True:
        if N==cnt:
            print(x+1, y+1)
            break
        board[y][x] = cnt
        cnt += 1
        
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or ny <0 or nx >=C or ny >= R or board[ny][nx]!=0:
            dir = (dir+1)%4
            nx = x + dx[dir]
            ny = y + dy[dir]
        x = nx
        y = ny
    