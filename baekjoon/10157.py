C, R = map(int, input().split())
N = int(input())

if N > C*R:
    print(0)
    exit()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 시작
x = 0
y = R - 1
dir = 0 # 0 1 2 3 # 상 우 하 좌

xmin = 0
xmax = C-1
ymin = 0
ymax = R-1
N -= 1
while True:
    if dir == 0:
        if y - ymin >= N:
            print(x+1, R-(y-N))
            break
        else:
            N -= y-ymin
            y = ymin
            dir = (dir+1)%4
            xmin += 1
    elif dir == 1:
        if xmax - x >= N:
            print(x+N+1, R-(y))
            break
        else:
            N -= xmax-x
            x = xmax
            dir = (dir+1)%4
            ymin += 1
    elif dir == 2:
        if ymax - y >= N:
            print(x+1, R-(N+y))
            break
        else:
            N -= ymax-y
            y = ymax
            dir = (dir+1)%4
            xmax -= 1
    elif dir == 3:
        if x - xmin >= N:
            print( x-N+1, R-(y))
            break
        else:
            N -= x-xmin
            x = xmin
            dir = (dir+1)%4
            ymax -= 1
