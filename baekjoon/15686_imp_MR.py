# Ch12_13
# boj 15686
# 핵심: 조합을 이용해서 다 해보기

import sys
from itertools import combinations

def getDistance(i1, j1, i2, j2):
    return abs(i1 - i2) + abs (j1 - j2)

N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

house_lst = []
chicken_lst = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken_lst.append((i,j))
        elif board[i][j] == 1:
            house_lst.append((i,j))

def getChickenDistance(ch: list, i, j):
    temp = int(1e9)
    for c in ch:
        temp = min(temp, getDistance(c[0], c[1], i, j))
    return temp

# print(chicken_lst)
# print(house_lst)

combi = list(combinations(chicken_lst, M))
# print(combi)
final_result = int(1e9)
for nowCom in combi:
    nowChickDistance = 0
    for house in house_lst:
        nowChickDistance += getChickenDistance(nowCom, house[0], house[1])
    
    final_result = min(final_result, nowChickDistance)


print(final_result)

"""

5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

"""


"""

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

"""