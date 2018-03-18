#!/bin/python3

import sys

def solve(n, p):
    front_counter=int(p/2)
    if n==p:
        back_counter=0
    elif n%2==1:
        back_counter=int((n-p)/2)
    else:
        back_counter=int((n-1-p)/2)+1

    if(front_counter<back_counter):
        return front_counter
    else:
        return back_counter


n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)