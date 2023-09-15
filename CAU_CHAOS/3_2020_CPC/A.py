import sys
input = sys.stdin.readline

N, K = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))  # 띄어쓰기 구분
    
newBoard = [ [-1 for i in range(N*K)] for j in range(N*K)]
for i in range(N):
    for j in range(N):
        stI = i*K
        stJ = j*K
        for ni in range(stI, stI+K):
            for nj in range(stJ, stJ+K):
                newBoard[ni][nj] = board[i][j]

for i in range(N*K):
    print(*newBoard[i])
    