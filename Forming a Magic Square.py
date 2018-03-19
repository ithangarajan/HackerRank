#!/bin/python3

import sys

magicMatrix =[]

def standardMatrix():
    tempMatrix=[]
    tempMatrix.append([8, 1, 6])
    tempMatrix.append([3, 5, 7])
    tempMatrix.append([4, 9, 2])

    magicMatrix.append(tempMatrix)

    tempMatrix=[]
    tempMatrix.append([6, 1, 8])
    tempMatrix.append([7, 5, 3])
    tempMatrix.append([2, 9, 4])
    magicMatrix.append(tempMatrix)

    tempMatrix=[]
    tempMatrix.append([4, 9, 2])
    tempMatrix.append([3, 5, 7])
    tempMatrix.append([8, 1, 6])
    magicMatrix.append(tempMatrix)

    tempMatrix=[]
    tempMatrix.append([2, 9, 4])
    tempMatrix.append([7, 5, 3])
    tempMatrix.append([6, 1, 8])

    magicMatrix.append(tempMatrix)

    tempMatrix=[]
    tempMatrix.append([8, 3, 4])
    tempMatrix.append([1, 5, 9])
    tempMatrix.append([6, 7, 2])
    magicMatrix.append(tempMatrix)

    tempMatrix=[]
    tempMatrix.append([4, 3, 8])
    tempMatrix.append([9, 5, 1])
    tempMatrix.append([2, 7, 6])
    magicMatrix.append(tempMatrix)

    tempMatrix=[]
    tempMatrix.append([6, 7, 2])
    tempMatrix.append([1, 5, 9])
    tempMatrix.append([8, 3, 4])
    magicMatrix.append(tempMatrix)

    tempMatrix=[]
    tempMatrix.append([2, 7, 6])
    tempMatrix.append([9, 5, 1])
    tempMatrix.append([4, 3, 8])
    magicMatrix.append(tempMatrix)


def formingMagicSquare(s):
    resultCost=999
    standardMatrix()
    for x in magicMatrix:
        resultMatrix=x
        cost=0
        for y in range(0,len(x)):
            for z in range(0,len(x[y])):
                cost=cost+ abs(x[y][z] - s[y][z])
        if (resultCost>cost):
            resultCost=cost
    return resultCost




if __name__ == "__main__":
    s = []
    for s_i in range(3):
       s_t = [int(s_temp) for s_temp in input().strip().split(' ')]
       s.append(s_t)
    result = formingMagicSquare(s)
    print(result)
