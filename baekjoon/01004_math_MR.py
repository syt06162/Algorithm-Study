import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, x2,y2 = map(int, input().split())
    N = int(input())
    in_1 = set()
    in_2 = set()
    for i in range(N):
        x,y, r = map(int, input().split())
        if ((x-x1)**2 + (y-y1)**2)**(1/2) < r:
            in_1.add(i)
        if ((x-x2)**2 + (y-y2)**2)**(1/2) < r:
            in_2.add(i)
    
    # 같은 개수 빼기
    n1 = len(in_1)
    n2 = len(in_2)
    n1n2 = len(in_1.intersection(in_2))
    print(n1 + n2 - n1n2*2)
    
            
        
