def star(N: int, flag: bool, qnum: int):
    if flag == False:
        for i in range(N):
            for j in range(N):
                QList[qnum+i].append(" ")
        
    else: #flag==true
        if N==1: 
            QList[qnum].append("*") 
            return

        for i in range(3):
            star(int(N/3), True,qnum)
        star(int(N/3), True, int(qnum + N/3))
        star(int(N/3), False, int(qnum + N/3))
        star(int(N/3), True, int(qnum + N/3))
        for i in range(3):
            star(int(N/3), True, int(qnum + N*2/3))

N = int(input())
QList = [[] for x in range(N)]

star(N, True, 0)

for i in range(N):
    for j in range(N):
        print(QList[i][j], end="")
    print("")