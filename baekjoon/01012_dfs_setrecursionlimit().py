import sys
sys.setrecursionlimit(52*52)
# M, N이 각각 최대 50이다. 최대 recursion의 개수를 생각해 보아야 하는데,
# dfs에서 상하좌우로 움직이므로 i<0 or i>=N, j<0 or j>=M 인 부분은 graph에서 모서리부분만큼이다. 
# (실제론 52*52보다 약간 작지만 계산하지 않고 넉넉히 줌)

di = [0,-1,0,1]
dj = [-1,0,1,0]

def dfs(graph, stI, stJ):
    graph[stI][stJ] = 0
    for k in range(4):
        nI, nJ = stI+di[k], stJ+dj[k]
        if nI<0 or nJ<0 or nI>=N or nJ>=M or graph[nI][nJ]==0:
            continue
        dfs(graph, nI, nJ)


T = int(input())
for _1 in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [ [0 for _3 in range(M)] for _4 in range(N) ]

    for _2 in range(K):
        j, i = map(int, sys.stdin.readline().split())
        graph[i][j] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                count += 1
                dfs(graph, i, j)

    print(count)