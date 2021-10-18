n, m = map(int, input().split())

topStart = n-m+1
topEnd = n

botStart = 1
botEnd = m

def count_num(start, end, num):
    currentNum = num
    cnt = 0
    while currentNum <= end:

        currentStart = start//currentNum * currentNum
        if currentStart != start:
            currentStart += currentNum

        currentEnd = end//currentNum * currentNum
        cnt += (currentEnd-currentStart)//currentNum + 1
        currentNum*=num
    
    return cnt


totalFive = count_num(topStart,topEnd,5) - count_num(botStart,botEnd,5)
totalTwo = count_num(topStart,topEnd,2) - count_num(botStart,botEnd,2)

#print("%d %d " % (count_num(topStart,topEnd,5), count_num(topStart,topEnd,2)))
#print("%d %d " % (count_num(botStart,botEnd,5), count_num(botStart,botEnd,2)))

print(min(totalTwo,totalFive))

