#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count=0
    orange_count=0
    for x in apples:
        if a+x >=s and a+x<=t:
            apple_count=apple_count+1
    for x in oranges:
        if b+x >=s and b+x<=t:
            orange_count=orange_count+1
    print (apple_count)
    print (orange_count)


if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
