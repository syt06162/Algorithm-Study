import sys
N = int(input())

# 입력 받기
dir = list()
leng = list()
for i in range(6):
    _dir, _leng = map(int, sys.stdin.readline().split())
    dir.append(_dir)
    leng.append(_leng)

# 최대값 (가로, 세로) 찾기
large_hori = 0
large_vert = 0
large_hori_idx = 0
large_vert_idx = 0

isLargest = [False, False, False, False, False, False]
for i in range(6):
    # 동서 최대값 찾기
    if (dir[i] in [1,2]) and (leng[i]>large_hori): #동,서
        large_hori = leng[i]
        large_hori_idx = i
    # 남북 최대값 찾기
    elif (dir[i] in [3,4]) and (leng[i] > large_vert):
        large_vert = leng[i]
        large_vert_idx = i
    
isLargest[large_vert_idx] = True
isLargest[large_hori_idx] = True

# 가로, 세로 최대값과 가장 멀리있는 2 개의 값이 큰사각형 - 작은사각형에서의 작은사각형 두 변.
for i in range(6):
    if isLargest[i%6] == True and isLargest[(i+1)%6] == True:
        # 작은 사각형 넓이를 구한다
        inRect = leng[(i+3)%6] * leng[(i+4)%6]
        break

# 전체 사각형에서 작은 사각형 넓이를 뺀다.
print((large_hori * large_vert - inRect)*N)
