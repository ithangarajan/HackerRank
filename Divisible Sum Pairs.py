#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    answer=0
    for x in range(0,len(ar)):
        for y in range(x,len(ar)):
            if (x != y):
                if ((ar[x]+ar[y])%k == 0):
                    answer=answer+1
    return answer
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
