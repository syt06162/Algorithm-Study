import sys

lst = []
for i in range(9):
    lst.append(list(map(int,sys.stdin.readline().split())))

def fun(stI, stJ, lst: list):
    numCount = [0 for i in range(10)] # 0~9
    zeroPos = []

    for k in range(0,9):
        hori = lst[stI][k]
        if hori == 0 and k != stJ:
            zeroPos.append((stI, k))
        else:
            numCount[hori] += 1

        verti = lst[k][stJ]
        if verti == 0 and k != stI:
            zeroPos.append((k, stJ))
        else:
            numCount[verti] += 1

    sqI, sqJ = (stI//3)*3, (stJ//3)*3
    for i in range(3):
        for j in range(3):
            nI, nJ = sqI+i, sqJ+j
            val = lst[sqI+i][sqJ+j]
            if val == 0 and (nI,nJ) != (stI,stJ):
                zeroPos.append((sqI+i, sqJ+j))
            else:
                numCount[val] += 1
    
    possibleNums = [x for x in range(1,10) if numCount[x]==0]

    if not possibleNums: # 되는 값이 하나도 없으면 그 앞의 가정이 잘못된 것.
        return False 

    if not zeroPos: # verti hori square 에서 0인 값이 하나도 없으면 stI, stJ에 알맞는 값을 집어넣고 리턴
        lst[stI][stJ] = possibleNums[0]
        return lst

    for num in possibleNums:
        lst[stI][stJ] = num
        flag = False
        for nextI, nextJ in zeroPos:
            if lst[nextI][nextJ] != 0:
                continue
            temp = fun(nextI, nextJ, lst)
            #print(stI,stJ, "넥스", nextI,nextJ)
            if temp:
                flag = True
                lst = temp
        
        if flag == False:
            lst[stI][stJ] = 0
#            return False
        return lst

    
for i in range(9):
    for j in range(9):
        if lst[i][j] == 0:
            print("")
            print("aa", i, j)
            lst = fun(i,j, lst)
            for k in range(9):
                print(*lst[k])            
            

for i in range(9):
    print(*lst[i])



'''
1 2 3 4 5 6 7 8 9
4 5 6 7 8 0 0 2 3
7 8 9 1 2 3 4 5 6
2 3 4 5 6 7 8 9 1
5 6 7 8 9 0 2 3 4
8 9 1 2 3 4 5 6 7
3 4 5 6 7 8 0 1 2
6 7 8 9 1 2 3 4 5
9 1 2 3 4 5 6 7 5

0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0


'''