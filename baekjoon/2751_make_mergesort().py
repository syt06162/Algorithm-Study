def mergeSort_2(arr: list):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left_arr = mergeSort_2(left)
    right_arr = mergeSort_2(right)
    
    lst = []
    left_idx = right_idx = 0
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            lst.append(left_arr[left_idx])
            left_idx += 1
        else:
            lst.append(right_arr[right_idx])
            right_idx += 1
    lst += left_arr[left_idx:]
    lst += right_arr[right_idx:]
    
    return lst

import sys

N = int(input())
lst = []
for i in range(N):
    lst.append(int(sys.stdin.readline()))
lst = mergeSort_2(lst)
for i in range(N):
    print(lst[i])