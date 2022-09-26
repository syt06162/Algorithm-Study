import sys
input = sys.stdin.readline

T = 0
while True:
    T += 1
    N, M = map(int, input().split())
    if N==0 and M==0:
        break
    
    # 유니온 파인드
    parent = [ i for i in range(N+1)]
    isTree = [ True for i in range(N+1)] # 일단은 True, 사이클 있으면 False
    
    def find_parent(a):
        if a!=parent[a]:
            parent[a] = find_parent(parent[a])
        return parent[a]
    
    def union(a, b):
        a = find_parent(a)
        b = find_parent(b)
        if a==b: # 사이클 !
            isTree[a] = False
        elif a>b:
            parent[a] = b
            if isTree[a] == False: # 이래야 나중 병합 사이클도 처리 !!
                isTree[b] = False
        else:
            parent[b] = a
            if isTree[b] == False:
                isTree[a] = False
    
    for i in range(M): 
        a,b = map(int, input().split())
        union(a,b)
    
    
    # 결과 계산
    result = 0
    for i in range(1,N+1):
        if i == find_parent(i) and isTree[i]: #즉, 루트인 경우 / 그중에서 그래프가 아니라 트리면
            result += 1
    
    # 출력
    print("Case %d:" % T, end=" ")
    if result == 0:
        print("No trees.")
    elif result == 1:
        print("There is one tree.")
    else:
        print("A forest of %d trees." % result)
    
    