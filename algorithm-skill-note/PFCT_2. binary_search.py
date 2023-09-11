def binary_search(arr, target, start, end): 
    # arr : sorted list
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            start = mid+1
        else: # arr[mid]>target
            end = mid-1
    return None

from bisect import bisect, bisect_left, bisect_right

lst = [1,2,5,5,7, 7,7,9,12,30]

print(bisect(lst, 7)) # 7
print(bisect_left(lst, 7)) # 4
print(bisect_right(lst, 7)) # 7
