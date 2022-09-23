def solution(n, k):
    fac = [factorial(i) for i in range(0,n)]
    
    nowLeft = n
    leftList = [i for i in range(1,n+1)]
    nowIdx = 0
    
    result = []
    while nowLeft != 0:
        for nowIdx in range(nowLeft):
            if k > fac[nowLeft - 1]:
                k -= fac[nowLeft - 1]
            else:
                temp = leftList[nowIdx]
                leftList.remove(temp)
                result.append(temp)
                
                nowLeft -= 1
                break
    
    return result

def factorial(n):
    if n==1 or n==0:
        return 1
    else: return n*factorial(n-1)
