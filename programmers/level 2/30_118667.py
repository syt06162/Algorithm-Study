# 그리디하게 매번 작은곳에서 pop
# 반복횟수가 핵심인데, len(q1)*2 보다 커야하는데...

def solution(qu1, qu2):
    
    from collections import deque
    
    q1 = deque(qu1)
    q2 = deque(qu2)
    
    length = len(q1)*2
    
    result = 0
    sumQ1 = sum(q1)
    sumQ2 = sum(q2)
    
    if sumQ1 == sumQ2:
        return result
    
    result += 1
    while result <= length*2:
        if sumQ1 < sumQ2:
            num = q2.popleft()
            q1.append(num)
            sumQ1 += num
            sumQ2 -= num
        else:
            num = q1.popleft()
            q2.append(num)
            sumQ2 += num
            sumQ1 -= num
        
        if sumQ1 == sumQ2:
            return result
        result += 1
        
    return -1
        