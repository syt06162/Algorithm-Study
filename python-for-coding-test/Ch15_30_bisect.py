# Ch15_30
# https://school.programmers.co.kr/learn/courses/30/lessons/60060
# 핵심 : 크기별로 나누고, 뒤집은배열, ?는 a 또는 z 로 치환

def solution(words, queries):
    # 앞 : Lwords
    Lwords = [[] for i in range(0, 10001)]
    for word in words:
        length = len(word)
        Lwords[length].append(word)
    for i in range(0, 10001):
        Lwords[i].sort()
    
    # 뒤집 : Lreverse
    N = len(words)
    Lreverse = [[] for i in range(0, 10001)]
    for i in range(0,10001):
        for word in Lwords[i]:
            temp = ""
            for j in range(len(word)-1, -1, -1):
                temp += word[j]
            Lreverse[i].append(temp)
    for i in range(0, 10001):
        Lreverse[i].sort()
    
    import bisect
    result = []
    for qry in queries:
        # 뒤
        if qry[0] == "?":
            Rqry = ""
            for j in range(len(qry)-1, -1, -1):
                Rqry += qry[j]
            
            qN = len(Rqry) 
            i = qN-1
            while i!=-1 and Rqry[i] == "?":
                i-=1
            
            left = Rqry[:i+1] + "a"*(qN-i-1)
            right = Rqry[:i+1] + "z"*(qN-i-1)
            
            result.append(bisect.bisect_right(Lreverse[qN], right) - bisect.bisect_left(Lreverse[qN], left))
        # 앞
        else:
            qN = len(qry) 
            i = qN-1
            while i!=-1 and qry[i] == "?":
                i-=1
            
            left = qry[:i+1] + "a"*(qN-i-1)
            right = qry[:i+1] + "z"*(qN-i-1)
            
            result.append(bisect.bisect_right(Lwords[qN], right) - bisect.bisect_left(Lwords[qN], left))
            
    return result