N, K = map(int, input().split())

count = 0
while True:
    while N%K==0:
        N //= K
        count += 1
    if N<K: break

    count += N%K
    N -= N%K
    
count += N-1
print(count)