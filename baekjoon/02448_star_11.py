N = int(input())

Qlist = []
for i in range(N-1):
    Qlist.append([" "*(N-i-1)])
Qlist.append([]) #null문자가 하나라도 있으면 오답이 되므로 별도로 리스트를 추가

def star_11(N: int, flag: bool, qnum: int):
    if flag == False:
        for i in range(N):
            Qlist[qnum+i].append(" "*(2*N-1-2*i))
        return

    if N==3:
        Qlist[qnum].append("*")
        Qlist[qnum+1].append("* *")
        Qlist[qnum+2].append("*****")
    else:
        half = N//2
        star_11(half, True, qnum)
        star_11(half, True, qnum + half)
        star_11(half, False, qnum + half)
        star_11(half, True, qnum + half)


star_11(N, True, 0)

for i in range(N-1): # 뒷부분에는 공백이 없는것처럼 보이지만 그렇게하면 또 오답이됨..
    Qlist[i].append(" "*(N-i-1))

for i in range(N):
    print(*Qlist[i], sep="")