def solution(a, b, n):
    result = 0
    left = n
    
    while left>=a:
        result += left//a*b
        left = left%a + left//a*b
    
    return result
        