# Ch13_20
# boj 18428
# 핵심: 그냥 해봄. 딥카피 굳이 안해도 됨.

from re import L
import sys

N = int(input())
board = []
for i in range(N):
    board.append(sys.stdin.readline().split())

Xlist = []
Slist = []
Tlist = []
for i in range(N):
    for j in range(N):
        if board[i][j] == "X":
            Xlist.append((i,j))
        elif board[i][j] == "S":
            Slist.append((i,j))
        else:
            Tlist.append((i,j))

from itertools import combinations
combiList = list(combinations(Xlist, 3))

# 선생 위치 기준 검사
di = [-1,1,0,0] #상하좌우
dj = [0,0,-1,1]

def findStudent(tempBoard, i,j):
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        while ni>=0 and ni<N and nj>=0 and nj<N:
            if tempBoard[ni][nj] == "O":
                break
            elif tempBoard[ni][nj] == "S":
                return True
            ni = ni + di[k]
            nj = nj + dj[k]
    return False


# 각각의 장애물 위치 모두 놓고, 감시확인
import copy
def result():
    for combi in combiList:
        tempBoard = copy.deepcopy(board)

        for i,j in combi:
            tempBoard[i][j] = "O"
        
        for ti, tj in Tlist:
            if findStudent(tempBoard, ti, tj) == True:
                break
        else:
            return True
    return False

if result()==True:
    print("YES")
else:
    print("NO")
