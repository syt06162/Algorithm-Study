import sys

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(0,N+1)]

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)
    if pa < pb:
        parent[b] = pa
    else:
        parent[a] = pb

for i in range(M):
    command, a, b= map(int, sys.stdin.readline().split())
    if command == 0:
        union(a,b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else: print("NO")

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1