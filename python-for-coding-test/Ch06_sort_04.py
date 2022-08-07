# N,K = 5,3
# a = [1,2,5,4,3]
# b = [5,5,6,6,5]
import sys
N,K = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)

#### 잘못된 풀이, b 배열에서의 선택 요소가 더 작은 경우는 바꾸지 않아야 함.
# sum2 = 0
# sum2 += sum(a[K:])
# sum2 += sum(b[-K:])
# print(sum2)

for i in range(K):
    if b[i] > a[i]:
        b[i] , a[i] = a[i], b[i]
    else:
        break

print(sum(a))