A, B, C = map(int, input().split())

def dnc(size):
    if size==1:
        return A %C
    
    half = dnc(size//2)
    if size%2==0:
        return (half*half) %C
    else:
        return (half*half*A) %C

print(dnc(B))