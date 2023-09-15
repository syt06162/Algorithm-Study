import sys
input = sys.stdin.readline

N = int(input())
board = [[0 for i in range(0, 365+1)] for j in range(N)]

lst = []
for i in range(N):
    s, e = map(int, input().split())
    lst.append([s,e])
lst.sort(key=lambda x: (x[0], -x[1]) )

# for i in range(N):
#     print(board[i][:15])

#넣기
for s,e in lst:
    for i in range(0, N):
        if board[i][s] == 0:
            break #i 부터
    for k in range(s, e+1):
        board[i][k] = 1

board_max = [0 for i in range(0, 365+1)]
for i in range(1, 365+1):
    maxVal = 0
    for k in range(N):
        if board[k][i]==1:
            maxVal = k+1
    board_max[i] = maxVal

# for i in range(N):
#     print(board[i][:15])

# print(board_max[:15])

cal = []
for i in board_max:
    if i==0:
        cal.append([])
    else:
        cal[-1].append(i)

answer = 0
for ls in cal:
    if len(ls) == 0:
        continue
    else:
        l = len(ls)
        m = max(ls)
        answer += l*m
print(answer)