from collections import deque

# 가능하면 visited를 꼭 쓰자! 안그러면 무한루프에 빠지거나, 엄청난 시간초과가 뜬다!
# 둘다 쓸 수 있는 상황이면 보통 bfs가 더 빠른 것 같다.

# dfs 는 심플하게 재귀
def dfs(graph: list, v:int, visited: list):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

# bfs에서 중요한 점은, visited=True 를 어디에 처리할지이다.
# Q에서 pop 하고나서 처리할 경우 여러개의 같은 것이 중복으로 Q에 들어가게 될 수도 있으니,
### 반드시 for문 안에서 Q에 삽입(append)할 때 visited를 True로 바꾸자.
def bfs(graph, start, visited):
    Q = deque()
    visited[start] = True
    Q.append(start)

    while Q:
        num = Q.popleft()
        print(num, end=" ")

        for i in graph[num]:
            if visited[i]==False:
                # visited true 처리하는 것의 위치 기억
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
