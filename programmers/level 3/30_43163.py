def solution(begin, target, words):
    if target not in words:
        return 0
    
    INF = int(1e9)
    N = len(words)
    
    def canGo(a, b):
        if len(a)!=len(b): 
            return False
        left = 1
        for i in range(len(a)):
            if a[i]!=b[i]:
                left -= 1
                if left==-1:
                    return False
        return True
    
    # BFS
    distance = dict()
    for word in words:
        distance[word] = INF
        
    from collections import deque
    Q = deque()
    
    for word in words:
        if canGo(word, begin):
            Q.append((1, word))
            distance[word] = 1
    
    while Q:
        dis, now = Q.popleft()
        for word in words:
            if distance[word] <= dis:
                continue
            if canGo(word, now):
                Q.append((dis+1, word))
                distance[word] = dis+1
    
    if distance[target] == INF:
        return 0
    else:
        return distance[target]