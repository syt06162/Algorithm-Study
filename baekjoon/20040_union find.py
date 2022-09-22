import sys
input = sys.stdin.readline

n,m = map(int, input().split())
parent = [i for i in range(n)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

cycle = -1
for i in range(m):
    a, b = map(int, input().split())
    if find_parent(a) != find_parent(b):
        union(a,b)
    elif cycle == -1:
        cycle = i

if cycle != -1:
    print(cycle + 1)
else:
    print(0)

