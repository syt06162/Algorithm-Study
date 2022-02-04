#******해결 완료******

def insertionSort(arr: list):
    # for 중첩문으로 해볼것
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

def insertionSort_2(arr: list):
    for i in range(1, len(arr)):
        j = i-1
        while j>=0:
            if arr[j+1]<arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                j -= 1
            else:                
                break

def insertionSort_3(lst:list):
    for i in range(1, len(lst)):
        j = i-1
        while lst[j]>lst[j+1] and j>=0:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            j -= 1

def bubbleSort(arr: list):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def bubbleSort_2(lst: list):
    for i in range(1, len(lst)):
        for j in range(i, 0, -1):
            if lst[j]<lst[j-1]:
                lst[j] , lst[j-1] = lst[j+1] , lst[j]


## 머지소트, 머지소트2 (pop(0)은 O(N)이므로 사용하지 않고 인덱스로 함)
def mergeSort(arr: list):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    l = mergeSort(left)
    r = mergeSort(right)
    
    lst = []
    while l and r:
        if l[0] < r[0]:
            lst.append(l.pop(0))
        else:
            lst.append(r.pop(0))
    
    while l:
        lst.append(l.pop(0))

    while r:
        lst.append(r.pop(0))
    return lst

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


# Quick sort 1: ShortCodes, 2: original

def quickSort_shortCodes(arr:list):
    if len(arr)<=1: 
        return arr
    pivot = arr[0] 
    left = [x for x in arr[1:] if x < pivot ]
    right = [x for x in arr[1:] if x >= pivot ]
    return quickSort_shortCodes(left) + [pivot] + quickSort_shortCodes(right)

def quickSort_original(arr):
    return quickSort_3_inputs(arr, 0, len(arr)-1)

# 퀵소트의 피벗을 가운데로 하면 ? 효율?

def quickSort_3_inputs(arr: list, start, end):
    if start >= end: return 
    
    i = start
    pivot = end

    for j in range(start, end):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]

    quickSort_3_inputs(arr, start, i-1)
    quickSort_3_inputs(arr, i+1, end)

def quickSort_pyBook(arr, start, end):
    if start >= end: return

    pivot = start
    left = start + 1
    right = end
    # print(arr[start:end+1])
    while left<=right: # tip: left랑 right가 같은 값일때는 절대 멈추면(스왑하면) 안된다. 그러면 무한루프에 빠짐.
        while left<=end and arr[left] <= arr[pivot]:
            left += 1
        while right>start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:    
            arr[left] , arr[right] = arr[right] , arr[left]
    
    quickSort_pyBook(arr, start, right-1)
    quickSort_pyBook(arr, right+1, end)
        
        


# Radix sort 를 위한 class Queue 

class Queue:
    def __init__(self, num):
        self.lst = []
        self.num = num
    
    def enQueue(self, val):
        self.lst.append(val)
    
    def deQueue(self):
        if len(self.lst) == 0:
            return -1
        else:
            return self.lst.pop(0)

Qlist = [Queue(i) for i in range(0,10)]

def radixSort(arr: list):
    # 자료구조 큐를 이용, 큐0~큐9까지 있음. 1의자리부터 비교, 1의자리가 0인건 큐0에, 1의자리가 1인건 큐1에 담음, 다시 뽑아내고 10의자리 비교
    Qlist = [Queue(i) for i in range(0,10)]
    maxLength = 0
    i = max(arr)
    while i:
        i//=10
        maxLength += 1

    iter = 0
    while iter < maxLength:
        for i in range(len(arr)):
            where = arr[i] // (10**iter) % 10
            Qlist[where].enQueue(arr[i])
        
        idx = 0
        for i in range(10):
            while True:
                temp = Qlist[i].deQueue()
                if temp == -1: break
                else: 
                    arr[idx] = temp
                    idx += 1
        iter += 1

####
def adjust_to_maxHeap(arr : list, start, end):
    parent = start
    child = 2*parent

    while child <= end:
        if child < end and arr[child] < arr[child+1]:
            child += 1
        if arr[parent] > arr[child]:
            break
        else:
            arr[parent], arr[child] = arr[child], arr[parent]
            parent = child
            child *= 2

def heapSort(arr: list):
    # arr[0] 은 비워두고 arr가 max heap 에서 출발 (adjust), arr[1] 맨뒤에 넣고 adjust, arr[2] 맨뒤두번째 넣고 adjust
    arr.insert(0, -1)  # 마지막에 pop(0)
   
    length = len(arr)
    for i in range((len(arr)-1)//2 , 0, -1):
        adjust_to_maxHeap(arr, i, length-1)
    for i in range(length-1, 0, -1):
        arr[1], arr[i] = arr[i], arr[1]
        adjust_to_maxHeap(arr, 1, i-1)
    
    arr.pop(0)


####

def gap_insertionSort(arr: list, first, last, gap):
    for i in range(first+gap, last+1, gap):
        temp = arr[i]
        j = i-gap
        while j>=0 and arr[j]>temp:
            arr[j+gap] = arr[j]
            j -= gap
        arr[j+gap] = temp
    

def shellSort(arr: list):
    gap = int(len(arr)/2)
    while gap >= 1:
        if gap%2 == 0 : gap += 1

        for i in range(0, gap):
            gap_insertionSort(arr, i, len(arr)-1, gap)

        gap //= 2




#**************************

arr = [11,1,6,7,5,2,8,6,10,3,1,7,4,0]
#insertionSort_2([5,2,6,3,1,4])
#insertionSort_2([5,2,8,6,10,3,1,7,4])
#bubbleSort(arr)
#print(mergeSort(arr))
#print(quickSort_shortCodes(arr))

#arr = [23,12,31,430,29,239,99,18,3123,9003]
#radixSort(arr)

#arr = [ 4, 3, 2, 5, 1]
#heapSort(arr)
#print(arr)

# shellSort(arr)
# print(arr)

quickSort_pyBook(arr,0,len(arr)-1)
print(arr)


