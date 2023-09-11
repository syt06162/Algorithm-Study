import sys

def find_parent(parent: list, x:int):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


# 입력받기
v, e = map(int, input().split())
parent = [0]*(v+1) #0번지는 사용하지 않음

for i in range(1, v+1):
    parent[i] = i

cycle = False
for i in range(e):
    a,b = map(int, sys.stdin.readline().split())

    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle: 
    print("사이클 발생함")
else:
    print("사이클 없음")

''' test case
5 4
4 5
3 4
2 3
1 2
'''

''' test case
6 4
1 4
2 3
2 4
5 6
'''

''' test case
3 3
1 2
2 3
1 3
'''