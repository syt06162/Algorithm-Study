import sys

N, M = map(int, sys.stdin.readline().split())
A, B, dir = map(int, sys.stdin.readline().split())

lst = []
for i in range(N):
    lst.append(list(map(int,sys.stdin.readline().split())))
# 육지 = 0, 땅 = 1, 가본육지 = -1
# for i in range(N):
#     print(lst[i])

dirA = [-1, 0, 1, 0]
dirB = [0, 1, 0, -1]


lst[A][B] = -1
count = 1
# totalCount = 1
while True:  
    # 책과의 시뮬레이션 차이점
    # 1. 방문기록배열을 따로 두지 않고 맵에 방문히면 -1기록, 
    # 2. turn_time변수를 쓰지 않고 매번 4방향확인, 약간 내 코드가 비효율적이다

    #print("(%d,%d), dir=%d, cnt=%d" % (A,B,dir,count))

    if lst[A + dirA[(dir-1)%4]][B + dirB[(dir-1)%4]] == 0: #왼쪽이 아직 안간 육지이면
        dir = (dir-1)%4
        A += dirA[dir]
        B += dirB[dir]
        lst[A][B] = -1 #간 육지로 기록
        count += 1 #새로운 방문일때만 count
        #totalCount += 1

    elif lst[A + dirA[dir]][B + dirB[dir]] != 0 and lst[A + dirA[(dir-2)%4]][B + dirB[(dir-2)%4]] != 0 \
    and lst[A + dirA[(dir-3)%4]][B + dirB[(dir-3)%4]] != 0 :  #4방향 모두 가봤거나 바다
        if lst[A + dirA[(dir-2)%4]][B + dirB[(dir-2)%4]] == 1: #뒷칸이 바다이면 종료
            break
        A += dirA[(dir-2)%4] #뒤로가기
        B += dirB[(dir-2)%4]
        # totalCount += 1

    else: #바로왼쪽은 비록 갈수없지만, 나머지 3 방향중 갈수있는곳이 있음
        dir = (dir-1)%4 #방향전환
        
print(count)
#print(totalCount)    


