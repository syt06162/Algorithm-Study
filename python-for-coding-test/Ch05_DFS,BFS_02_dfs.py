'''
입력을 받는데 1로 감싸게 입력받음
받아서 1,1부터 끝까지 반복문 -> if val ==0: cnt ++, dfs

'''
def dfs(graph, i,j):
    if graph[i][j]==1:
        return
    graph[i][j] = 1
    dfs(graph,i-1,j)
    dfs(graph,i,j-1)
    dfs(graph,i+1,j)
    dfs(graph,i,j+1)
    
import sys

N, M = map(int, input().split())
lst = []
lst.append([1 for _ in range(M+2)])
for _ in range(N):
    lst.append([1] + list(map(int, sys.stdin.readline().strip())) + [1])
lst.append([1 for _ in range(M+2)])

count = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if lst[i][j] == 0:
            count += 1
            dfs(lst, i,j)

print(count)
