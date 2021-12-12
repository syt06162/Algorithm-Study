import sys

N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

def fun(startI, startJ, size):
    cnt = [0, 0, 0] # 0, 1, -1 집합의 개수
    c = lst[startI][startJ]
    if size == 1:
        cnt[c] += 1
        return cnt
    
    for i in range(startI, startI + size):
        for j in range(startJ, startJ + size):

            if lst[i][j] != c:
                s = size//3
                for ni in range(3):
                    for nj in range(3):
                        temp = fun(startI + s*ni, startJ + s*nj, s)
                        cnt[0] += temp[0]
                        cnt[-1] += temp[-1]
                        cnt[1] += temp[1]
                return cnt
        
    cnt[c] += 1
    return cnt


result = fun(0,0,N)
print(result[-1])
print(result[0])
print(result[1])