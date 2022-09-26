def solution(fees, records):
    basicM , basicP, moreM, moreP = fees
    
    recordDict = dict()
    
    # 파싱 및 데이터 저장
    for record in records:
        lst = list(record.split())
        time = lst[0]
        what = lst[1]
        
        if what not in recordDict:
            recordDict[what] = []
        
        recordDict[what].append(time)
    
    # 홀수개 데이터 out 처리
    for record in recordDict:
        if len(recordDict[record])%2==1:
            recordDict[record].append("23:59")
    
    # 각각의 데이터 요금 청구
    recordList = list(recordDict)
    recordList.sort()
    
    resultList = []
    for record in recordList:
        timeList = recordDict[record]
        length = len(timeList)
        i=0
        totalTime = 0
        while i!=length:
            inTime = timeList[i]
            outTime = timeList[i+1]
            inLst = list(map(int,inTime.split(":")))
            inM = inLst[0]*60+inLst[1]
            outLst = list(map(int,outTime.split(":")))
            outM = outLst[0]*60+outLst[1]
            totalTime += outM-inM
            i += 2
        if totalTime <= basicM:
            resultList.append(basicP)
        else:
            temp = (totalTime-basicM)//moreM
            if temp != (totalTime-basicM)/moreM:
                temp += 1
            result = basicP + temp*moreP
            resultList.append(result)
    return resultList
        