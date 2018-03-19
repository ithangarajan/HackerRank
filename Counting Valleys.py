#!/bin/python3

import sys

def countingValleys(n, s):
    level=0
    valley_start=0
    number_of_valley=0
    for x in range(0,len(s)):
        if s[x]=="U":
            level=level+1
        elif s[x]=="D":
            level=level-1
        if level == -1 and valley_start == 0:
            valley_start=1
        if level == 0 and valley_start==1:
            number_of_valley=number_of_valley+1
            valley_start=0
    return (number_of_valley)
if __name__ == "__main__":fs
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)