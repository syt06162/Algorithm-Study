import sys

N, M= map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(trees)
target = M

def binary_search(arr, target, start, end): 
    result = 0
    while start <= end:
        cuts = 0
        mid = (start+end)//2
        for tree in arr:
            if tree>mid:
                cuts += tree-mid
        
        if cuts >= target:
            start = mid+1
            result = mid
        else : # cuts < target
            end = mid-1
            
    return result

print(binary_search(trees, target, start, end))