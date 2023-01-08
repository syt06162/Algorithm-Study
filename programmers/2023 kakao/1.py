def solution(today, terms, privacies):
    
    todayList = list(map(int, today.split(".")))
    todayNum = todayList[0]*10000 + todayList[1]*100 + todayList[2]
    pagiList = []
    
    # term 저장
    termDict = dict()
    for i in terms:
        a, b = i.split()
        termDict[a] = int(b)
        
    def isPagi(date, pri):
        dateList = list(map(int, date.split(".")))
        dateList[1] += termDict[pri]
        if dateList[1] >= 13:
            dateList[0] += dateList[1]//12 
            dateList[1] = dateList[1]%12 
            if dateList[1] ==0:
                dateList[1] = 12
                dateList[0] -= 1
        # 비교
        dateNum = dateList[0]*10000 + dateList[1]*100 + dateList[2]
        if dateNum > todayNum:
            return False
        return True
    
    # 하나하나 파기 여부 판별
    for i in range(len(privacies)):
        pri = privacies[i]
        date, types = pri.split()
        if isPagi(date, types)==True:
            pagiList.append(i+1)
    return pagiList
    
