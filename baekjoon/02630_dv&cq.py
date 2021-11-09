import sys

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

def cutting(startI, startJ, size):
    color = lst[startI][startJ]

    if size == 1:
        counting[color] += 1
        return 
    
    for i in range(startI, startI+size):
        for j in range(startJ, startJ+size):
            if lst[i][j] != color:
                break
        if lst[i][j] != color:
                break
    else: # 모든 색이 같으면
        counting[color] += 1
        return
    
    # 색이 다른경우 반으로 나눠 각각 함수 실행
    half = size//2
    cutting(startI, startJ, half)
    cutting(startI+half, startJ, half)
    cutting(startI, startJ+half, half)
    cutting(startI+half, startJ+half, half)

counting = [0, 0]
cutting(0,0,N)
print(counting[0])
print(counting[1])
