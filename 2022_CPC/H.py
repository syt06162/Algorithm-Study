import sys
input = sys.stdin.readline
# 시간이 오래 걸리니 pypy3로 제출

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

# 애들 위치 구하기
regList = []
sinPos = [] # 처음위치
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        elif board[i][j] == 1:
            regList.append([i,j])
        else:
            sinPos = [i,j]

# 다 깰 수 있는지 없는지 여부
sinMod = (sinPos[0] + sinPos[1])%2
for i,j in regList:
    if (i+j)%2 != sinMod:
        print("Shorei")
        break
else:
    print("Undertaker")
    # 브루트 포스 - permutation

    minResult = int(1e9)
    from itertools import permutations
    for regPerm in permutations(regList, len(regList)):
        # 두 점 사이 거리 = max(i-i1, j-j1)
        nowResult = 0
        nowY, nowX = sinPos
        for newY, newX in regPerm:
            nowResult += max(abs(nowX-newX) , abs(nowY-newY))
            nowY, nowX = newY, newX
        
        minResult = min(minResult, nowResult)
    print(minResult)