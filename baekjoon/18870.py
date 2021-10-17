import sys

N = int(input())

lst = list(map(int, sys.stdin.readline().split()))

rankLst = sorted(list(set(lst)))
dic = {rankLst[i]: i for i in range(len(rankLst))}

for i in lst:
    print(dic[i], end=" ")