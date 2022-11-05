def solution(food):
    for i in range(1,len(food)):
        if food[i]%2==1:
            food[i] -= 1
        food[i] //= 2
    
    resultList = []
    for i in range(1, len(food)):
        for j in range(food[i]):
            resultList.append(i)
    
    resultList = resultList + [0] + sorted(resultList, reverse=True)
    resultStr = ""
    for r in resultList:
        resultStr += str(r)
    return resultStr
    