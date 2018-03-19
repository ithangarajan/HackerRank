#!/bin/python3

import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    if x==y and y==z:
        return "Mouse C"
    elif x==z:
        return "Cat A"
    elif y==z:
        return "Cat B"

    catone_steps=0
    cattwo_steps=0

    if x>z:
        catone_steps=x-z
    else:
        catone_steps = z - x

    if y>z:
        cattwo_steps=y-z
    else:
        cattwo_steps = z - y

    if (catone_steps==cattwo_steps):
        return "Mouse C"
    elif (catone_steps>cattwo_steps):
        return "Cat B"
    elif (catone_steps<cattwo_steps):
        return "Cat A"


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])
        result = catAndMouse(x, y, z)
        f.write(result + '\n')
    f.close()