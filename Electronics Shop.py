#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    price_list=[]
    purchase=0
    for x in range(0,len(keyboards)):
        for y in range(0,len(drives)):
            price_list.append(keyboards[x]+drives[y])
    price_list.sort()
    if price_list[0]>s:
        return -1
    else:
        for x in range(0,len(price_list)):
            if price_list[x]>s:
                break
            purchase = price_list[x]
        return purchase

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)