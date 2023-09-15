import sys
input = sys.stdin.readline

def shuffle(pos, arr):
    dir = 0 # 0=왼쪽 1오른쪽
    if pos>13:
        dir = 1
        pos -= 13
    
    # 왼쪽경우
    left = pos
    result = 0
    
    if dir == 0:
        for i in range(len(arr)):
            if i%2==1:
                if left>=arr[i]:
                    result += arr[i]
                    left -= arr[i]
                else:
                    result += left
                    left = 0
            else:
                result += arr[i]
            if left==0:
                break
    else:
        for i in range(len(arr)):
            if i%2==0:
                if left>=arr[i]:
                    result += arr[i]
                    left -= arr[i]
                else:
                    result += left
                    left = 0
            else:
                result += arr[i]
            if left==0:
                break
            
    return result

N = int(input())
pos = 1
for i in range(N):
    lst = list(map(int, input().split()))
    pos = shuffle(pos, lst)
print(pos)





        
    