#!/bin/python3

import sys

def solve(n, s, d, m):
    answer=0
    for x in range(0,len(s)):
        sum=0
        if (x+m<=n):
            for y in range(x,x+m):
                sum=sum+s[y]
        if (sum == d):
            answer = answer+1
    return answer

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
