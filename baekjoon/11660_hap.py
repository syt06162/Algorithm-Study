import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

hap = [[0 for i in range(N)] for i in range(N)]

#1열 1행은 직접
rowSum = 0
colSum = 0
for i in range(N):
    rowSum += board[0][i]
    hap[0][i] = rowSum
    
    colSum += board[i][0]
    hap[i][0] = colSum

# (1,1)부터 하나씩 올라가면서
for i in range(1,N):
    for j in range(1,N):
        hap[i][j] = hap[i-1][j] + hap[i][j-1] - hap[i-1][j-1] + board[i][j]
#왼쪽에 0 확장
newHap = [[0 for i in range(N+1)] for i in range(N+1)]
for i in range(0,N):
    for j in range(0,N):
        newHap[i+1][j+1] = hap[i][j]

# 입력받아 처리
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sums = newHap[x2][y2] - newHap[x1-1][y2] - newHap[x2][y1-1] + newHap[x1-1][y1-1]
    print(sums)
    