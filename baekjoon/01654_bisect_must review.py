import sys

K, N = map(int, sys.stdin.readline().split())
lst = []
for i in range(K):
    lst.append(int(sys.stdin.readline()))
lst.sort()

start = 1
end = lst[-1]

result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in range(K):
        count += lst[i]//mid  #자른 개수 총합
    
    if count < N:
        end = mid - 1
    elif count >= N:
        start = mid + 1
        result = max(mid, result)        

print(result)

#result 없이 그냥 print(end) 해도 되지만 직관적으로 더 정확함.