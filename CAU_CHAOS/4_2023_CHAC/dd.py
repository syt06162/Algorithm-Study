import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

right_streak = [1 for i in range(N)]
left_streak = [1 for i in range(N)]
# left
for i in range(1,N):
    if lst[i] > lst[i-1]:
        left_streak[i] = left_streak[i-1] + 1
# right
for i in range(N-2,-1,-1):
    if lst[i] < lst[i+1]:
        right_streak[i] = right_streak[i+1] + 1

# print(right_streak)
# print(left_streak)
ans = K
for i in range(N-K+1):
    st = K
    # left streak
    if i!=0:
        before = lst[i-1]
        beforelow = 0
        beforehigh = 0
        for j in range(i, i+K):
            if lst[j] < before:
                beforelow += 1
            else:
                beforehigh += 1
        st = max(st, beforehigh + left_streak[i-1])

    # right streak
    if i!=N-K:
        after = lst[i+K]
        afterlow = 0
        afterhigh = 0
        for j in range(i, i+K):
            if lst[j] < after:
                afterlow += 1
            else:
                afterhigh += 1
        st = max(st, afterlow + right_streak[i+K])
        
    
    # two streak
    if i !=0 and i!=N-K:
        if beforehigh == K and afterlow == K:
            st = left_streak[i-1] + right_streak[i+K] + K
    
    ans = max(ans, st)

print(ans)
    