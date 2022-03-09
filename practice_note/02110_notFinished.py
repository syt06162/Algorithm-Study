import sys

N, C = map(int, sys.stdin.readline().split())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()

first = lst[0]
last = lst[-1]
targets = []
for i in range(C):
    targets.append(first + (last-first) * i / (C-1))

# print(targets)

results = []
for target in targets: # target을 lst에서 bisect 해서 start, end 중 더 가까운 쪽의 값을 result에 넣어준다.
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        val = lst[mid]
        if val == target:
            start = mid # while문 이후에 lst[start] 또는 lst[end] 값을 넣어줄건데, lst[mid] 값을 넣어주기 위함
            break
        elif val < target:
            start = mid + 1
        elif val > target:
            end = mid - 1 

    a = lst[start]
    b = lst[end]
    if abs(target-a) < abs(target-b):
        results.append(a)
    else:
        results.append(b)

# print(results)

mini = results[1]-results[0]
for i in range(2, len(results)):
    temp = results[i] - results[i-1]
    if temp < mini:
        mini = temp
        
print(mini)
