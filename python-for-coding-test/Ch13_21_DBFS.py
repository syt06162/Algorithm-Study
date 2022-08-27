# Ch13_21
# boj 16234
# 핵심: 연합표, 연합함수, dfs 비슷한 함수
# 제출시: recursion set, pypy3 제출
import sys
sys.setrecursionlimit(2501)

N, L , R = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

# 연합 표
union = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        union[i][j] = i*N+j+1

# 연합 계산 함수
dy = [-1,1,0,0] # 상하좌우
dx = [0,0,-1,1]
def findUnion():
    # 초기화
    for i in range(N):
        for j in range(N):
            union[i][j] = 0

    val = 0
    for y in range(N):
        for x in range(N):
            val += 1
            if union[y][x] == 0:
                union[y][x] = val
                spread(val, y, x)
            
def spread(val, y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny>=0 and ny<N and nx>=0 and nx<N and union[ny][nx]==0 \
        and (L <= abs(board[y][x] - board[ny][nx]) <= R):
            union[ny][nx] = val
            spread(val, ny, nx)

# 이동 함수
def moves():
    uniList = dict()
    uniCount = dict()
    for y in range(N):
        for x in range(N):
            team = union[y][x]
            if team not in uniList:
                uniList[team] = board[y][x]
                uniCount[team] = 1
            else:
                uniList[team] += board[y][x]
                uniCount[team] += 1
    # n빵
    for key in list(uniList.keys()):
        uniList[key] = uniList[key] // uniCount[key]
    
    # 골고루 사람 이동
    for y in range(N):
        for x in range(N):
            board[y][x] = uniList[ union[y][x] ]

def isSame(beforeBoard, board):
    for i in range(N):
        for j in range(N):
            if beforeBoard[i][j] != board[i][j]:
                return False
    return True

cnt = 0
while True:   
    import copy
    beforeBoard = copy.deepcopy(board)

    findUnion()
    moves()
    cnt += 1

    if isSame(beforeBoard, board) == True:    
        cnt -=1
        break

print(cnt)