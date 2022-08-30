# Ch15_28

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def bisect():
    start = 0
    end = N-1
    while start<=end:
        mid = (start + end)//2
        if nums[mid] == mid:
            return mid
        elif nums[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(bisect())