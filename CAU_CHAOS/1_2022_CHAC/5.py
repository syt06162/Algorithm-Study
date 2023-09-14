import sys
input = sys.stdin.readline

# union find
N, M = map(int, input().split())

parent = [i for i in range(N+1)] #0번지 사용 안함
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    a,b = map(int, input().split())
    union_parent(a,b)


arr = list(map(int, input().split()))

result = 0
# 테스트
for i in range(1, N):
    if find_parent(arr[i]) != find_parent(arr[i-1]):
        result += 1
print(result)