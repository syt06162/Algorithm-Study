from itertools import combinations
# 될확률
lst = [0.183529412,
0.177669903,
0.191428571,
0.06,
0.290322581,
0.135,
]
co = [i for i in range(len(lst))]

ans = [0.0 for i in range(len(lst)+1)]
for i in range(len(lst)+1):
    coLst = list(combinations(co,i))
#    print(coLst)
    for currentCo in coLst:
        temp = 1.0
        for j in range(len(lst)):
            if j in currentCo:
                temp *= lst[j]
            else:
                temp *= 1-lst[j]
        ans[i]+= temp
    

for j in range(len(ans)):
    print("%d개 이관될 확률 : %f%%" % (j, ans[j]*100))
print("계 = %f" % (sum(ans)))