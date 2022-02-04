from collections import deque

# 가능하면 visited를 꼭 쓰자! 안그러면 무한루프에 빠지거나, 엄청난 시간초과가 뜬다!

def dfs(graph: list, v:int, visited: list):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    Q = deque()
    visited[start] = True
    Q.append(start)

    while Q:
        num = Q.popleft()
        print(num, end=" ")

        for i in graph[num]:
            if visited[i]==False:
                visited[i] = True
                Q.append(i)


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
print("dfs: ", end="")
dfs(graph,1,visited)

print("")

visited = [False] * 9
print("dfs: ", end="")
bfs(graph,1,visited)
