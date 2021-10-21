import sys

N, M, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

# line 6~17 : max_1, max_2 를 구하는 방법. O(n)이다. 책은 sort쓰므로 최악이 O(nlogn)
max_1 = max(lst[0], lst[1]) 
max_2 = min(lst[0], lst[1])
for i in range(2, N):
    if lst[i]<=max_2:
        continue
    else:
        if lst[i] > max_1:
            max_2 = max_1
            max_1 = lst[i]
        else:
            max_2 = lst[i]

# line 20~ 답 구하는 과정. O(1)
if max_1 == max_2:
    ans = max_1 * M
else:
    ans = (M//(K+1)) * (K*max_1 + max_2) + (M%(K+1)) * max_1
print(ans)
