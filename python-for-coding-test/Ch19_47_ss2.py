import copy
import sys
input = sys.stdin.readline
# 개빡구현.

N = 4
dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]
board = [[] for i in range(N)] # -1은빈곳, 99는 상어, 그외는 물고기
shark = [-1,-1,-1] # y,x, dir

for i in range(N):
    j = 0
    lst = list(map(int, input().split()))
    while j<2*N:
        board[i].append([lst[j], lst[j+1]-1]) # 물고기번호, dir
        j += 2


result = 0
# 최초 이팅
nowFish, nowDir = board[0][0][0], board[0][0][1]
shark = [0,0, nowDir]
board[0][0] = [99, nowDir] # 기존상어위치 빈칸으로 두는 것도 잊지 말것
result += nowFish

def getFishPose(board, num):
    for i in range(N):
        for j in range(N):
            if board[i][j][0] == num:
                return [i,j]
    return [-1,-1]

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

def allFishMoving(board):
    for i in range(1,N*N+1):
        y,x = getFishPose(board, i)
        if y!=-1: # 찾은경우 - 이동
            dir = board[y][x][1]
            for k in range(0,8):
                ny = y + dy[(dir+k)%8]
                nx = x + dx[(dir+k)%8]
                if ny<0 or nx<0 or ny>=N or nx>=N or board[ny][nx][0]==99:
                    continue
                
                dir = (dir+k)%8
                board[ny][nx], board[y][x] = board[y][x], board[ny][nx]
                board[ny][nx][1] = dir
                break


def dfs(board, shark, result):
    
    # 물고기 이동하고
    allFishMoving(board)
    y,x,dir = shark
    

    # 최대 결과 기록
    resultList = [result]
    for k in range(1,4):
        ny = y + dy[dir]*k
        nx = x + dx[dir]*k
        if ny<0 or nx<0 or ny>=N or nx>=N:
            break
        if board[ny][nx][0] == -1:
            continue
        
        b = copy.deepcopy(board)
        s = copy.deepcopy(shark)
        t_result = result + board[ny][nx][0]
        # 새 보드, 샤크 갱신 후 dfs에 돌리기
        newdir = b[ny][nx][1]
        b[y][x] = [-1,0]
        b[ny][nx] = [99, newdir]
        s = [ny,nx,newdir]
        resultList.append( dfs(b,s,t_result) )
    
    return max(resultList)


print(dfs(board, shark, result))