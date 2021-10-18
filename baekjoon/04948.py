MAX = 123456*2
lst = [0 for x in range(0,2*123456+1)] #0이 소수, 1이 합성수 // 0, 1, ..., 2N
p = 2
while p*p <= MAX:
    if lst[p] == 0:
        i=p
        while i*p <= MAX:
            lst[i*p] = 1
            i += 1
    p += 1

N = int(input())
while N!=0:
    count = 0
    for i in range(N+1, 2*N+1):
        if lst[i] == 0:
            count += 1
    print(count)
    
    N = int(input())