# 2차원 구간합 계산
# 한번에 여러개 처리 후 최종 쓸기
# 프로그래머스 92344 문제 참조

from copy import deepcopy

N = 5
M = 10
board = [[0 for i in range(M)] for j in range(N)]

# 1,1 부터 3,5 까지 8로 만들기

startY, startX = 1,1
endY, endX = 3,5

imosBoard = deepcopy(board)
imosBoard.append([0 for i in range(M)])
for i in range(0,N+1):
    imosBoard[i].append(0)

val = 8
# 핵심 4곳 찍기 !!!!!
imosBoard[startY][startX] = val
imosBoard[startY][endX + 1] = - val
imosBoard[endY + 1][startX] = - val
imosBoard[endY + 1][endX + 1] = val

# 좌우 휩쓸기
for i in range(0, N+1):
    for j in range(1, M+1):
        imosBoard[i][j] += imosBoard[i][j-1]

# 상하 휩쓸기
for j in range(0, M+1):
    for i in range(1, N+1):
        imosBoard[i][j] += imosBoard[i-1][j]

# debug - imosBoard
for i in range(0,N+1):
    print(imosBoard[i])
print()

# board에 += 갱신
for i in range(0, N):
    for j in range(0, M):
        board[i][j] += imosBoard[i][j]

# debug - board
for i in range(0,N):
    print(board[i])