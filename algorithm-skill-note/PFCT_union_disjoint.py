import sys

# union find 핵심 기억할것
# 1. 함수들 원형 외우기
# 2. 반드시! 함수 외 부분에서는 parent[a] 직접 사용 X, find_parent(a) 로 사용 O !!!!
#    그래야 정렬과 동시에 find가 된다. 반드시 find_parent() 함수로만 사용!


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

for i in range(e):
    a,b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b) #아직까지는 바로 윗부모 (루트가 아닐수도 있음)를 가리키지만,

print("원소번호 :")
for i in range(1, v+1):
    print(i, end=" ")
print()

print("각 원소가 속한 집합 :")
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ") # 이 과정에서 부모들이 루트노드로 갱신된다
print()

print("얘네의 부모 :")
for i in range(1, v+1):
    print(parent[i], end=" ")
print()


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