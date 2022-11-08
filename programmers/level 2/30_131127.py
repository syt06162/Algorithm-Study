
def solution(want, number, discount):
    # 투포인터 알고리즘
    result = 0
    
    # 첫 시작일까지 계산
    N = len(want)
    wantDict = dict()
    for i in range(N):
        w = want[i]
        wantDict[w] = number[i]
    
    disDict = dict()
    # 10일까지 합
    for w in want:
        disDict[w] = 0
    for i in range(0,10):
        w = discount[i]
        if w in disDict:
            disDict[w] += 1
        else:
            disDict[w] = 1
            
    # 일치하는지
    def isOK():
        for w in want:
            if wantDict[w] != disDict[w]:
                return False
        return True
    
    if isOK():
        result += 1
    
    # 끝까지 반복
    if len(discount)==10: return result
    for i in range(10, len(discount)):
        w = discount[i]
        if w in disDict:
            disDict[w] += 1
        else:
            disDict[w] = 1
        
        disDict[discount[i-10]] -= 1
        if isOK():
            result += 1
    return result
        
        