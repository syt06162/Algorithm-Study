import sys

N = int(input())
lst = []
arrP = [0 for _ in range(0,4001)] #빈도를 구하는 배열 중 양수, 0
arrM = [0 for _ in range(0,4001)] #빈도를 구하는 배열 중 음수 (arrM[0]은 사용되지 않음)

for _ in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
    if num >= 0:
        arrP[num] += 1
    else:
        arrM[-num] += 1

lst.sort()

most = max(max(arrP) , max(arrM)) #빈도 배열의 최대값
flag = 0 #최대값이 여러개이면 아래에서 두번째 값 선택
for i in range(4000,0,-1):
    if arrM[i] == most:
        idx = -i
        flag += 1
        if flag == 2: break
if flag != 2:
    for i in range(0,4001):
        if arrP[i] == most:
            idx = i
            flag += 1
            if flag == 2: break

print(round(sum(lst)/N)) #평균
print(lst[N//2]) #중앙값
print(idx) #최빈값
print(max(lst) - min(lst)) #범위