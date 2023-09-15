import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 보드에 dp
for i in range(N-2, -1, -1):
    for j in range(0,M):
        if board[i][j] == 0:
            continue
        else:
            temp = 0
            if j!=0:
                temp += board[i+1][j-1]
            temp += board[i+1][j]
            if j!=M-1:
                temp += board[i+1][j+1]
            board[i][j] = temp

print((sum(board[0]))%1000000007)
