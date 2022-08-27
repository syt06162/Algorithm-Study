# Ch12_12
# https://school.programmers.co.kr/learn/courses/30/lessons/60061
# 핵심: 매 행동마다 전체체크 코드를 구현하면 편함. 시간 충분.

def solution(n, build_frame):
    bo = [[0 for i in range(n+1)] for j in range(n+1)]
    gidoong = [[0 for i in range(n+1)] for j in range(n+1)]
    
    for command in build_frame:
        x,y, what, isBuild = command
        
        if what==0 and isBuild==1:
            gidoong[y][x] = 1
            if isOK(n, bo, gidoong)==False:
                gidoong[y][x] = 0
        
        elif what==0 and isBuild==0:
            gidoong[y][x] = 0
            if isOK(n, bo, gidoong)==False:
                gidoong[y][x] = 1
                
        elif what==1 and isBuild==1:
            bo[y][x] = 1
            if isOK(n, bo, gidoong)==False:
                bo[y][x] = 0
                
        elif what==1 and isBuild==0:
            bo[y][x] = 0
            if isOK(n, bo, gidoong)==False:
                bo[y][x] = 1
    
    result = []
    for j in range(n+1):
        for i in range(n+1):
            if gidoong[i][j]==1:
                result.append((j,i,0))
            if bo[i][j]==1:
                result.append((j,i,1))
    return result

def isOK(n, bo, gidoong):
    for i in range(n+1):
        for j in range(n):
            if bo[i][j] == 1:
                if (i!=0 and (gidoong[i-1][j]==1 or gidoong[i-1][j+1])) or (j!=0 and j!=n-1 and bo[i][j-1]==1 and bo[i][j+1]==1):
                    continue
                else:
                    return False
                
    for i in range(n+1):
        for j in range(n+1):
            if gidoong[i][j] == 1:
                if i==0 or gidoong[i-1][j]==1 or (j!=0 and bo[i][j-1]==1) or (j!=n and bo[i][j]==1):
                    continue
                else:
                    return False
    return True