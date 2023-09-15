import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for i in range(N+1)]
newGraph = [[] for i in range(N+1)]

addcnt = 0
addStart = N+1
for i in range(1,N+1):
    inp = input().strip()
    if inp == "0":
        continue

    lst = list(map(int, inp.split()))

    cnt = lst[0]
    graph[i] = lst[1:]
    newGraph[i] = lst[1:]

    if cnt > M:
        addnow = (cnt-1)//M
        mod = cnt % M
        addcnt += addnow

        gangList = []
        newListList = []
        for i in range(addnow):
            gangList.append(addStart + i)
            newListList.append(graph[i][i*M:i*M+M])
        newGraph[i] = gangList
        newGraph.extend(newListList)
        addStart += addnow
        addcnt += addnow # 재귀?

print(newGraph)
print(addcnt)

# print(graph)


