#!/bin/python3

import sys

def pickingNumbers(a):
    maxCount=0
    for x in range(0,len(a)):
        count=0
        lesser_count=0
        greater_count=0
        equal_count=0
        for y in range(0,len(a)):
            if x!=y:
                if (a[x]-a[y]) == -1:
                    greater_count=greater_count+1
                elif (a[x]-a[y]==1):
                    lesser_count=lesser_count+1
                elif (a[x]==a[y]):
                    equal_count=equal_count+1
        if (lesser_count>=greater_count):
            count=lesser_count+equal_count+1
        else:
            count=greater_count+equal_count+1
        if(maxCount<count):
            maxCount=count
    return maxCount

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)