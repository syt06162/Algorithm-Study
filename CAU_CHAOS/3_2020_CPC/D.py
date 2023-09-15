import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

milkList = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            milkList.append([i, j])
        elif board[i][j] == 1:
            hi = i
            hj = j
            
def get_distance(i,j, ni, nj):
    return abs(i-ni) + abs(j-nj)

from itertools import permutations
perms = permutations(milkList, len(milkList))

result = 0
for perm in perms:
    ni = hi
    nj = hj
    nHealth = M
    answer = 0
    possible_list = [0]
    
    # print(perm)
    for mi, mj in perm:
        dist = get_distance(ni, nj, mi, mj)
        if nHealth >= dist:
            answer += 1
            nHealth += H
            nHealth -= dist
            ni = mi
            nj = mj
            # print(ni, nj, hi, hj)
            if nHealth >= get_distance(ni, nj, hi, hj):
                possible_list.append(answer)
        else:
            break
    maxval = max(possible_list)
    # print(possible_list)
    result = max(result, maxval)

print(result)
            
