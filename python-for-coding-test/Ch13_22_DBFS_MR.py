# Ch13_22
# https://school.programmers.co.kr/learn/courses/30/lessons/60063
# 핵심: bfs 여러 상황 다 고려

def isEnd(y,x, N):
    if y==N-1 and x==N-1: return True

def solution(board):
    N = len(board)
    
    from collections import deque
    Q = deque()
    dir = 0 # 0:좌우 , 1:상하
    y0, x0 = 0,0
    y1, x1 = 0,1
    visitedSet = set()
    visitedSet.add((y0,x0, y1,x1))
    
    second = 0
    Q.append((y0,x0, y1,x1,dir, second))
    
    # Q돌기 - bfs
    dy = [-1,1,0,0] #상하좌우
    dx = [0,0,-1,1]
    
    while Q:
        y0,x0, y1,x1, dir, second = Q.popleft()
        if dir == 0:
            for k in range(4):
                ny0 = y0 + dy[k]
                ny1 = y1 + dy[k]
                nx0 = x0 + dx[k]
                nx1 = x1 + dx[k]
                # 이동 불가능
                if ny0<0 or ny1<0 or ny0>=N or ny1>=N or nx0<0 or nx1<0 or nx0>=N or nx1>=N or board[ny0][nx0]==1 or board[ny1][nx1]==1 or ((ny0,nx0,ny1,nx1) in visitedSet) or ((ny1,nx1,ny0,nx0) in visitedSet):
                    continue
                    
                # 이동가능 
                if isEnd(ny0, nx0, N) or isEnd(ny1, nx1, N):
                    return second+1
                else:
                    Q.append((ny0,nx0, ny1,nx1,dir, second+1))
                    visitedSet.add((ny0,nx0, ny1,nx1))
                    # 회전도 처리
                    if k == 0: # 상
                        Q.append((y0,x0,y0-1,x0,1, second+1))
                        visitedSet.add((y0,x0,y0-1,x0))
                        Q.append((y1,x1,y1-1,x1,1, second+1))
                        visitedSet.add((y0,x0,y0-1,x0))
                    elif k == 1: #하
                        Q.append((y0,x0,y0+1,x0,1, second+1))
                        visitedSet.add((y0,x0,y0+1,x0))
                        Q.append((y1,x1,y1+1,x1,1, second+1))
                        visitedSet.add((y1,x1,y1+1,x1))
                        
        elif dir == 1:
            for k in range(4):
                ny0 = y0 + dy[k]
                ny1 = y1 + dy[k]
                nx0 = x0 + dx[k]
                nx1 = x1 + dx[k]
                # 이동 불가능
                if ny0<0 or ny1<0 or ny0>=N or ny1>=N or nx0<0 or nx1<0 or nx0>=N or nx1>=N or board[ny0][nx0]==1 or board[ny1][nx1]==1 or ((ny0,nx0,ny1,nx1) in visitedSet) or ((ny1,nx1,ny0,nx0) in visitedSet):
                    continue
                    
                # 이동가능 
                if isEnd(ny0, nx0, N) or isEnd(ny1, nx1, N):
                    return second+1
                else:
                    Q.append((ny0,nx0, ny1,nx1,dir, second+1))
                    visitedSet.add((ny0,nx0, ny1,nx1))
                    # 회전도 처리
                    if k == 2: # 좌
                        Q.append((y0,x0,y0,x0-1,0, second+1))
                        visitedSet.add((y0,x0,y0,x0-1))
                        Q.append((y1,x1,y1,x1-1,0, second+1))
                        visitedSet.add((y1,x1,y1,x1-1))
                    elif k == 3: # 우
                        Q.append((y0,x0,y0,x0+1,0, second+1))
                        visitedSet.add((y0,x0,y0,x0+1))
                        Q.append((y1,x1,y1,x1+1,0, second+1))
                        visitedSet.add((y1,x1,y1,x1+1))
    