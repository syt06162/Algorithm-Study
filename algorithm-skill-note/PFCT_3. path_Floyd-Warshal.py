import sys
input = sys.stdin.readline
INF = int(1e9) #10억

# V, E 입력받기
V = int(input())
E = int(input())

### V+1 크기의 2차원 그래프 생성, 모두 무한대 값으로 넣어줌 (0번 vertex는 사용하지 않음)
graph = [ [ INF for _1 in range(V+1) ] for _2 in range(V+1) ]
for i in range(1,V+1):
    graph[i][i] = 0


### 간선에 대한 정보 입력 받기. a에서 b로 가는 비용이 c이면, (a, b, c)
for i in range(E):
    a,b,c = map(int, input().split())
    graph[a][b] = c


#### 플로이드 워셜 알고리즘 !!! ★★★
for i in range(1, V+1):
    for j in range(1,V+1):
        for k in range(1,V+1):
            graph[j][k] = min( graph[j][i] + graph[i][k] , graph[j][k] )


# 최종 결과 출력, INF인 경우 -1 출력하기
for i in range(1, V+1):
    for j in range(1, V+1):
        if graph[i][j] == INF:
            print("%3d" % -1, end=" ")
        else:
            print("%3d" % graph[i][j], end=" ")
    print("")


'''
test case

4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

'''