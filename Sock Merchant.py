#!/bin/python3

import sys

def sockMerchant(n, ar):
    used=[]
    counter=0
    for x in range(0,len(ar)):
        used.append(0)
    for x in range(0,len(ar)):
        for y in range(x,len(ar)):
            if (x != y):
                if (ar[x]==ar[y] and used[x]==0 and used[y]==0):
                    counter=counter+1
                    used[x]=1
                    used[y]=1
    return counter

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)