#!/bin/python3

import sys

def hurdleRace(k, height):
    maxHeight=0
    for x in height:
        if maxHeight<x:
            maxHeight=x
    if maxHeight<=k:
        return 0
    else:
        return maxHeight-k


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)