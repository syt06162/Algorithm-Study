import sys
input = sys.stdin.readline

N = int(input())
time_dict = dict()
for _ in range(N):

    for time in [4,6,4,10]:
        lst = list(input().split())
        for person in lst:
            if person =="-":
                continue
            else:        
                if person in time_dict:
                    time_dict[person] += time
                else:
                    time_dict[person] = time

lst = list(time_dict.values())
if len(lst) == 0:
    print("Yes")
    exit()
    
lst.sort()
minVal = lst[0]
maxVal = lst[-1]

if maxVal - minVal <= 12:
    print("Yes")
else:
    print("No")

# print(time_dict)
