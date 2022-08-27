# Ch13_23
# boj 10825
# 핵심: sort() 를 한번만 사용하므로, 감소순인 것들은 수 앞에 - 붙이기


import sys

N = int(input())
students = []
for i in range(N):
    name, a,b,c = sys.stdin.readline().split()
    students.append((name, -int(a), int(b), -int(c)))

students.sort(key=lambda x: (x[1], x[2], x[3], x[0]))
for i in range(N):
    print(students[i][0])