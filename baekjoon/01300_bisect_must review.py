N = int(input())
k = int(input())
#혼자 힘으로 풀지 못하고 백준 질문창에서 힌트를 봤음... 복습하자

def getLowOrEqualNums(num: int):
    count = 0
    for i in range(1, N+1):
        count += min(N, num//i)
    return count

start = 1
end = N*N
result = 0
while start<=end:
    mid = (start + end) // 2
    val = getLowOrEqualNums(mid)
    # print("a",start, end, mid, val )
    if val >= k:
        result = mid
        end = mid - 1
    elif val < k:
        start = mid + 1 

print(result)