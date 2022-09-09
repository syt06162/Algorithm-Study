import sys

input = sys.stdin.readline
N, K = map(int, input().split())
nums = list(map(int, input().split()))

hap = []
l = 0
r = K-1
sums = sum(nums[l:r+1])
hap.append(sums)
while r+1<N:
    sums -= nums[l]
    l += 1
    
    r += 1
    sums += nums[r]
    hap.append(sums)
print(max(hap))
    
