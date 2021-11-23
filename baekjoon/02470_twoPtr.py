import sys

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

start = leftVal = 0
end = rightVal = N-1
currentValue = abs(lst[start]+lst[end])

while start < end:
    value = lst[start]+lst[end]
    if abs(value)<currentValue:
        currentValue = abs(value)
        leftVal = start
        rightVal = end

    if value > 0:
        end -= 1
    else:
        start += 1
        
print(lst[leftVal], lst[rightVal])