lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# from itertools import combinations
# result = list(combinations(lst, 4))
# for re in result:
#     print(*re, sep="")
# print(len(result), "len")

def combi(lst: list, k:int ):
    if k==1:
        return lst

    result = []
    n = len(lst)
    for i in range(0, n-k+1):
        tailLst = combi(lst[i+1:], k-1)
        for tail in tailLst:
            result.append(lst[i] + tail)
    return result

result2 = combi(lst, 4)
for re in result2:
    print(*re, sep="")
print(len(result2), "len")