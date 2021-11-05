# N,K = 5,3
# a = [1,2,5,4,3]
# b = [5,5,6,6,5]
import sys
N,K = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort()

sum2 = 0
sum2 += sum(a[K:])
sum2 += sum(b[-K:])
print(sum2)