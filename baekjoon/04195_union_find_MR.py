import sys
input = sys.stdin.readline

# union find 를 쓰는데, 친구 이름에 대해서 0,1,2로 딕셔너리 사용

T = int(input())
for _ in range(T):
    
    friendNumDict = dict()
    frinedCount = 0
    parent = []
    childCount = []

    def find_parent(x):
        if x!=parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(x,y):
        x = find_parent(x)
        y = find_parent(y)
        if x > y:
            parent[x] = y
            childCount[y] += childCount[x]
        elif y > x:
            parent[y] = x
            childCount[x] += childCount[y]
        # else 즉 같은 경우는 child 값 변화가 없도록 무시.

    
    F = int(input())
    for i in range(F):
        a, b = input().split()
        if a not in friendNumDict:
            friendNumDict[a] = frinedCount
            parent.append(frinedCount)
            childCount.append(1)
            frinedCount += 1
        if b not in friendNumDict:
            friendNumDict[b] = frinedCount
            parent.append(frinedCount)
            childCount.append(1)
            frinedCount += 1
        
        aNum = friendNumDict[a]
        bNum = friendNumDict[b]
        union(aNum, bNum)
        print(childCount[find_parent(aNum)])
