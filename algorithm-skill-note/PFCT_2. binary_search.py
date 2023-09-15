# lst : sorted list
lst = [1,2,5,5,7, 7,7,9,12,30]

def bisect_mine(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target: # 그냥 mid가 아니라 arr[mid] !!!
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(bisect_mine(0, len(lst), 7)) # 중복에 대한 처리는 없음


from bisect import bisect, bisect_left, bisect_right

print(bisect(lst, 7)) # 7
print(bisect_left(lst, 7)) # 4
print(bisect_right(lst, 7)) # 7
