#!/bin/python3

import sys

def hackerrankInString(s):
    check = "hackerrank"
    counter=0
    result=""
    for x in range(0,len(s)):
        if (check[counter] == s[x]):
            result = result + s[x]
            counter = counter+1
            if counter > (len(check)-1):
                break
    if result == check:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)