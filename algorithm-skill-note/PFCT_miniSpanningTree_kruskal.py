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

edges = []
result = 0 # sum of cost (result)

for i in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        result += cost

print(result)


''' test case
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
''' # 159