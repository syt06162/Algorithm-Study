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

