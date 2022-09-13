# Ch18_41
# union find, 직접구현은 안됨. (바로 연결은 아니어도, 돌아가서 연결인 경우를 처리 못함)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))
trip = list(map(int, input().split()))

parent = [i for i in range(N)]

def find_parent(a):
    if a != parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b :
        parent[b] = a
    else:
        parent[a] = b
        
# board로 parent 합집합 하기
for i in range(len(board)):
    row = board[i]
    for num in row:
        if num==1:
            union_parent(i, num)

# 경로 결과값
answerFlag = True
now = trip[0] - 1  # 예제는 1 2 3 4, 내 코드는 0 1 2 3 이므로.
for i in range(1, M):
    next = trip[i] - 1
    if find_parent(now) != find_parent(next):
        answerFlag = False
        break


if answerFlag == True:
    print("YES")
else: 
    print("NO")

# print(parent) -> 예제에서는 0 0 0 0 0