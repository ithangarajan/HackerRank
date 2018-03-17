#!/bin/python3

import sys

def migratoryBirds(n, ar):
    list_of_numbers=[]
    list_of_frequency=[]
    for x in range(0,len(ar)):
        if (ar[x] in list_of_numbers):
            for y in range(0,len(list_of_numbers)):
                if list_of_numbers[y]==ar[x]:
                    break;
            list_of_frequency[y]= list_of_frequency[y] + 1
        else:
            list_of_numbers.append(ar[x])
            list_of_frequency.append(0)
    max_frequency=0
    for x in range(0,len(list_of_frequency)):
        if list_of_frequency[x]>max_frequency:
            max_frequency = list_of_frequency[x]
    return (list_of_numbers[list_of_frequency.index(max_frequency)])


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)