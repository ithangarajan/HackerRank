#!/bin/python3

import sys

def minimumNumber(n, password):
    s=password
    uppercounter =0
    lowercounter =0
    digitcounter=0
    specialcounter=0
    specialstring = "!@#$%^&*()-+"
    result=0
    for x in range(0,len(s)):
        if (s[x].isupper()):
            uppercounter = uppercounter+1
        elif (s[x].islower()):
            lowercounter = lowercounter+1
        elif (s[x].isdigit()):
            digitcounter = digitcounter+1
        elif (specialstring.find(s[x])):
            specialcounter = specialcounter+1

    if uppercounter ==0:
        result = result+1
    if lowercounter ==0:
        result = result+1
    if digitcounter ==0:
        result = result+1
    if specialcounter ==0:
        result = result+1
    if n+result<6:
        result = result + (6-(n+result))
    return result


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
