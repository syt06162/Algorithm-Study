import sys
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

px = -1
py = -1
legi = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            px = j
            py = i
        elif board[i][j] == 1:
            legi.append((i,j))

#가능한지
mods = (px+py)%2
for y,x in legi:
    hap = (y+x)%2
    if hap != mods:
        print("Shorei")
        exit()
print("Undertaker")

# 브루트포스 perms
from itertools import permutations
perms = permutations(legi, len(legi))

answer = int(1e9)
opx = px
opy = py
for perm in perms:
    px = opx
    py = opy
    sums = 0
    for ly,lx in perm:
        dist = max(abs(ly-py), abs(lx-px))
        sums += dist
        px = lx
        py = ly
    answer = min(answer, sums)
print(answer)

