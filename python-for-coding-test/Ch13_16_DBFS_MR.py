# Ch13_16
# boj 14502
# 핵심: dfs 브루트포스

from collections import deque
import sys

# 입력받기
N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

# 추가 벽 조합 구하기
isZero = []
isTwo = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            isZero.append((i,j))
        elif board[i][j] == 2:
            isTwo.append((i,j))

from itertools import combinations
combiList = list(combinations(isZero, 3))

# 복사하고 벽쳐본거의 안전지역(0) 카운트
def zeroCount():
    count = 0
    for i in range(N):
        for j in range(M):
            if tempBoard[i][j] == 0:
                count += 1
    return count


# dfs로 바이러스 퍼뜨려보기
dy = [-1,1,0,0] #상하좌우 
dx = [0,0,-1,1]

def dfs(y, x):
    tempBoard[y][x] = 2
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ny<0 or ny>=N or nx<0 or nx>=M:
            continue
        if tempBoard[ny][nx] == 0:
            dfs(ny,nx)


# 모든 조합의 경우를 다 체크해본다.
result = 0
for combi in combiList:
    import copy
    tempBoard = copy.deepcopy(board)

    # 3개 벽 쳐보기
    for y,x in combi:
        tempBoard[y][x] = 1
    
    # 퍼뜨리기
    for y,x in isTwo:
        dfs(y,x)
    
    # 0 카운트 해서 적은거 취하기
    result = max(zeroCount(), result)

print(result)
