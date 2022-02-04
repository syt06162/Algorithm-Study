lst = ['a', 'b', 'c', 'd', 'e', 'f']

# from itertools import permutations
# result = list(permutations(lst, 3))
# for re in result:
#     print(*re, sep="")
# print(len(result), "len")

def permu(lst: list, k:int ):
    if k==1:
        return lst

    result = []
    n = len(lst)
    for i in range(0, n):
        tailLst = permu(lst[:i] + lst[i+1:], k-1)
        for tail in tailLst:
            result.append(lst[i] + tail)
    return result

result2 = permu(lst, 3)
for re in result2:
    print(*re, sep="")
print(len(result2), "len")