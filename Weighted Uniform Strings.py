#!/bin/python3

import sys

possible_list = []

def print_check(s):
    abcd="abcdefghijklmnopqrstuvwxyz"
    result=""
    value_list=[]
    max_value=len(s)
    for x in range(0,max_value):
        if result.find(s[x])== -1:
            result=result+s[x]
    for x in range(0,len(result)):
        value_list.append(s.count(result[x]))
    #print (value_list)
    for x in range(0,len(result)):
        for y in range(1,value_list[x]+1):
            possible_list.append((abcd.find(result[x])+1)*y)

def check_result(num):
    for x in possible_list:
        if num==x:
            return "Yes";
    return "No";



s = input().strip()
n = int(input().strip())
print_check(s)
for a0 in range(n):
    x = int(input().strip())
    print (check_result(x))