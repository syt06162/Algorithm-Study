N = 5 # 데이터 개수
M = 5 # 찾고자 하는 부분합 M
data = [1, 2 , 3, 2 ,5]

count = 0
interval_sum = 0
end = 0

for start in range(N):
    # start 부터 end-1 까지 포함하는 합
    while interval_sum < M and end < N:
        interval_sum += data[end]
        end += 1
    
    if interval_sum == M:
        count += 1
    
    interval_sum -= data[start]

print(count)