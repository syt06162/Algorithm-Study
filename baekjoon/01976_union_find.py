import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

parent = [i for i in range(N)]

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

for i in range(N):
    for j in range(0, i):
        if graph[i][j] == 1:
            union(i, j)

# test
test = list(map(int, input().split()))
for i in range(0, M-1):
    if find_parent(test[i]-1) != find_parent(test[i+1]-1):
        print("NO")
        break
else:
    print("YES")