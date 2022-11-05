def solution(X, Y):
    N = 10
    xCnt = [0 for i in range(N)]
    yCnt = [0 for i in range(N)]
    for i in X:
        xCnt[int(i)] += 1
    for i in Y:
        yCnt[int(i)] += 1
        
    # -1 판별
    for i in range(N):
        if xCnt[i]!=0 and yCnt[i]!=0:
            break
    else:
        return "-1"
    
    # 위부터 세서 대입
    result = ""
    for i in range(N-1,-1,-1):
        iter = min(xCnt[i], yCnt[i])
        result += str(i)*iter
            
    if result[0]=="0" and result[-1]=="0":
        return "0"
    else: return result
        