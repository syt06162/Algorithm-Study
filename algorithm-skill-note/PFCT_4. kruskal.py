import sys
input = sys.stdin.readline

V, E = map(int, input().split())
parent = [i for i in range(V+1)]
edges = []
for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# find_parent, union_parent
def find_parent(x):
    if x!=parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

edges.sort()

result = 0
for cost, a, b in edges:
    pa = find_parent(a)
    pb = find_parent(b)
    if pa!=pb:
        union(pa, pb)
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
''' 
# 159