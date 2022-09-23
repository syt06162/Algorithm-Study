def solution(w,h):
    # 최소공배수 구하기
    from math import gcd
    
    # w에 작은 수 두기
    if w>h:
        w,h = h,w
        
    blockNum = gcd(w,h) # 한 블럭의 화이트 개수
    
    oneBlockSum = (h//blockNum) + (w//blockNum) - 1
    result = w*h - oneBlockSum * blockNum
    return result