import sys
input = sys.stdin.readline

N = int(input())
A,B,C,D,E,F = map(int, input().split())

X = 0
for i in range(1,N+1):
    if i%A == 0:
        X += i
    # print(X, "A")
    if i%B == 0:
        X %= i
    # print(X, "B")
    if i%C == 0:
        X = X & i
    #print(X, "C")
    if i%D == 0:
        X ^= i
    # print(X, "D")
    if i%E == 0:
        X |= i
    # print(X, "E")
    if i%F == 0:
        X >>= i
    # print(X, "F")
print(X)