from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [[] for i in range(N)]
for i in range(N):
    what = list(map(int, input().split()))
    for j in what:
        board[i].append([j, 0, 0]) #누구, 향주인, 남은기간

# 상어들
sharks = [[i, 0,0, 0] for i in range(0,M+1)] #누구, y,x, dir
sharks[0] = [-1,-1,-1,-1]
temp = list(map(int, input().split()))
for i in range(1,M+1):
    sharks[i][3] = temp[i-1]
for i in range(N):
    for j in range(N):
        if board[i][j][0] != 0:
            who = board[i][j][0]
            sharks[who][1] = i
            sharks[who][2] = j
sharkCount = M

# 우선순위
sharkRank = [[] for i in range(M+1)]
for k in range(1,M+1):
    sharkRank[k].append([])
    for i in range(4):
        sharkRank[k].append(list(map(int, input().split())))

dy = [9, -1,1,0,0]
dx = [9, 0,0,-1,1]

# 초기 냄새
for who, y, x, dir in sharks:
    if who == -1:
        continue
    board[y][x] = [who, who, K]
    
# 이동
second = 0
while second<=1000 and sharkCount>1:
    second += 1
    

    beforePosList = []
    for i in range(1,M+1):
        if sharks[i][0] == -1:
            continue
        
        dir = sharks[i][3]        
        rankList = sharkRank[i][dir]
        y = sharks[i][1]
        x = sharks[i][2]
        # 이동 준비
        blankList = []
        myList = []
        for k in rankList:
            ny = y + dy[k]
            nx = x + dx[k]
            if ny<0 or ny>=N or nx<0 or nx>=N:
                continue
            else:
                whose = board[ny][nx][1]
                if whose == i:
                    myList.append((ny,nx, k))
                elif whose == 0:
                    blankList.append((ny,nx, k))
        if not blankList:
            blankList = myList
            
        # 상어를 임시이동
        sharks[i] = [i, blankList[0][0], blankList[0][1], blankList[0][2]]
        beforePosList.append((y,x))
        
    for y,x in beforePosList:
        board[y][x][0] = 0
        
    # 중복상어들 우위
    for who, y, x, dir in sharks:
        if who == -1:
            continue
        for j in range(who+1, M+1):
            aI, aY, aX, aDir = sharks[j]
            if aI == -1: continue
            
            if (y==aY and x==aX):
                sharks[j][0] = -1
                sharkCount -= 1
        board[y][x][0] = who
    
    
    # 향 줄어들기
    for i in range(N):
        for j in range(N):
            if board[i][j][2] != 0:
                board[i][j][2] -= 1
                if board[i][j][2] == 0:
                   board[i][j][1] = 0 

    # 냄새뿌리기
    for who, y, x, dir in sharks:
        if who > 0:
            board[y][x] = [who, who, K]
    
if second>1000:
    print(-1)
else:
    print(second)