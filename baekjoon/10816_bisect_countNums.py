import sys

N = int(input())
numLst = list(map(int, sys.stdin.readline().split()))
numLst.sort()

M = int(input())
findLst = list(map(int, sys.stdin.readline().split()))

def binary_search_right(arr, target, start, end): 
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid+1
        else: # arr[mid] > target:
            end = mid-1
    return start #마지막 오른쪽 그 다음값

def binary_search_left(arr, target, start, end): 
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else: # arr[mid] >= target:
            end = mid-1
    return end #마지막 왼쪽 그 앞값

def binary_search(arr, target, start, end): 
    
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return start, end, mid
        elif arr[mid]<target:
            start = mid+1
        else:
            end = mid-1
    return -1, -1, -1


for target in findLst:
    start, end, mid = binary_search(numLst, target, 0, N-1)
    if mid == -1:
        print(0, end=" ")
    else:
        l = binary_search_left(numLst, target, start, end)
        r = binary_search_right(numLst, target, start, end)
        
        print(r-l-1, end=" ")