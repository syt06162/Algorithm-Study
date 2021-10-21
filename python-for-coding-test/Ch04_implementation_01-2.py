N = int(input())

cnt = 0
for h in range(0,N+1):
    if h%10==3:
        cnt += 60*60
    else:
        m=59
        while m>=0:
            if m%10==3 or m//10==3:
                cnt += 60
            else:
                s = 59
                while s>=0:
                    if s%10==3 or s//10==3:
                        cnt+=1
                    s-=1
            m -= 1
    
print(cnt)
        