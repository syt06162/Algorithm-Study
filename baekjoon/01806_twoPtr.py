import sys
INF = 100001

N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
sumLst = [0]
for i in range(0, N):
    sumLst.append(sumLst[i] + lst[i])

left = 0 
right = 1
result = INF

while left < N:
    hap = sumLst[right] - sumLst[left] #left~right-1 까지의 합. right은 항상 더할것 다음 값을 가리킴
    if hap >= S:
        temp = right - left
        if temp < result: #더 작은 길이가 있으면 넣기
            result = temp
        left += 1
    elif hap < S and right < N:
        right += 1
    else:
        left += 1 

if result == INF:
    print(0)
else:
    print(result)