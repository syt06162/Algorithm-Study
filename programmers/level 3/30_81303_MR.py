def solution(n, k, cmd):
    linkDict = dict()
    for i in range(n):
        linkDict[i] = [i-1, i+1]
    
    cutList = []
    now = k
    for command in cmd:
        if len(command) >= 3:
            what = command[0]
            how = command[2:]
            
            val = 1 # down
            if what=="U":
                val = 0
            for i in range(int(how)):
                now = linkDict[now][val]
        else: # C나 Z
            if command[0]=="C":
                prev,next = linkDict.pop(now)
                if prev in linkDict:
                    linkDict[prev][1] = next
                if next in linkDict:
                    linkDict[next][0] = prev
                cutList.append([now, prev,next])
                if next in linkDict:
                    now = next
                else:
                    now = prev
            else: # Z
                where ,prev, next = cutList.pop()
                if prev in linkDict:
                    linkDict[prev][1] = where
                if next in linkDict:
                    linkDict[next][0] = where
                linkDict[where] = [prev, next]
    
    result = ""
    for i in range(n):
        if i in linkDict:
            result+="O"
        else:
            result+="X"
    return result
                
                
                
                