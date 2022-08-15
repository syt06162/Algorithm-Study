import sys
N, M = map(int, input().split())
dduk = list(map(int, sys.stdin.readline().split()))

# 굳이 sort 하고 마지막값을 할 필요 없이, 그냥 max로. (sort의 경우 nlogn)
maxi = max(dduk)

# bisect 변환 - 핵심: beforeOkay라는 것의 존재여부, 그리고 위치 (sums가 타겟보다 작을때는 x)
def bisect(arr, start, end, target):
    while start<=end:
        mid = (start+end)//2

        sums = 0
        for i in arr:
            if i>= mid:
                sums += i - mid

        if sums == target:
            return mid
        elif sums < target:
            end = mid - 1
        else:
            beforeOkay = mid
            start = mid + 1
    return beforeOkay

result = bisect(dduk, 0, maxi, M)
print(result)
