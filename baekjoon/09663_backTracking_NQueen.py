dr = [-1,-1,1,1]
dc = [-1,1,1,-1]

N = int(input())
graph = [[0]*N for i in range(N)] #0은 빈공간, 1은 퀸 놓은 위치
horizentalCheck = [0] * N # - 방향(수평방향) 체크
plusDiagonalCheck = [0] * (2*N-1) # / 방향 대각선체크, r+c = 일정
minusDiagonalCheck = [0] * (2*N-1) # \ 방향 대각선체크, r-c+N-1 = 일정
count = 0


def checkOK(row, column): # 그 위치에 놓을 수 있으면 True, 아니면 False
    if horizentalCheck[row] or plusDiagonalCheck[row+column] or minusDiagonalCheck[row-column+N-1]:
        return False
    # 다 체크해봤는데 퀸이 걸리는게 없으면 이 자리에 놓을 수 있음
    return True
    

def dfs(column: int):
    global count
    if column == N:
        count += 1
        return

    for row in range(N):
        # graph[row][column] 에 퀸을 놓을수 있는지 보고, 가능하다면 놓고 다음 과정
        if checkOK(row, column):
            horizentalCheck[row] = 1
            plusDiagonalCheck[row+column] = 1
            minusDiagonalCheck[row-column+N-1] = 1
            graph[row][column] = 1
            dfs(column+1)
            horizentalCheck[row] = 0
            plusDiagonalCheck[row+column] = 0
            minusDiagonalCheck[row-column+N-1] = 0
            graph[row][column] = 0


dfs(0)
print(count)