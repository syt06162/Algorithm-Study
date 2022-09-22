import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N)]
stars = []

def find_parent(a):
    if a!=parent[a]:
        parent[a] = find_parent(parent[a])
    return parent[a]
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(N):
    x,y = map(int, input().split())
    stars.append((x,y))

# 이미 연결
for i in range(M):
    a,b = map(int, input().split())
    if find_parent(a-1) != find_parent(b-1):
        union(a-1,b-1)

edges = []
for i in range(0,N):
    x1,y1 = stars[i]
    for j in range(0,i):
        if find_parent(i) == find_parent(j):
            continue
        x2,y2 = stars[j]
        cost = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        edges.append((cost, i,j))
edges.sort()

result = 0
# 크루스칼
for cost, a,b in edges:
    if find_parent(a) != find_parent(b):
        union(a,b)
        result += cost
print(format(result,".2f"))