import sys
input = sys.stdin.readline

KK = int(1e9)+7
N, M= map(int, input().split())

if M==1:
    ans = pow(2, N, KK) - 1
    print(ans%KK)
else:
    ans = 0
    ans += (-2*M-1)%KK
    tmp = (pow(2, N+1, KK) * M%KK) % KK

    ans += tmp

    print(ans%KK)