# Ch15_27

import sys

N, x = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

def bisect_first(target: int, start, end):
    while start <= end:
        mid = (start + end)//2

        # target 발견! - 그러나 맨 왼쪽일때만 리턴
        if nums[mid] == target and (mid==0 or nums[mid-1] <target):
            return mid

        elif nums[mid] < target:
            start = mid + 1
        
        # else에 nums[mid] == target인 경우도 포함 : end를 줄여야함 (bisect_first 한정)
        else:
            end = mid - 1
    return -1

def bisect_last(target: int, start, end):
    while start <= end:
        mid = (start + end)//2

        # target 발견! - 그러나 맨 오른쪽일때만 리턴
        if nums[mid] == target and (mid==N-1 or nums[mid+1] > target):
            return mid

        # nums[mid] == target인 경우에는 : start를 올려야함 (bisect_last 한정)
        elif nums[mid] <= target:
            start = mid + 1
        
        else:
            end = mid - 1
    return -1

# 결과
last = bisect_last(x,0,N-1)
if last != -1:
    print(last - bisect_first(x, 0 , N-1) + 1)
else:
    print(-1)