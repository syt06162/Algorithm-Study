def recursion(s, l, r, count):
    if l >= r: return (1, count+1)
    elif s[l] != s[r]: return (0, count+1)
    else: return recursion(s, l+1, r-1, count+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    st = input().strip()
    result, count = isPalindrome(st)
    print(result, count)