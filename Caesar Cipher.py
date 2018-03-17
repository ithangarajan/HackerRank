#!/bin/python3

import sys

def replace_char(input,rotate):
    abcd="abcdefghijklmnopqrstuvwxyz"
    abcd_caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if abcd.find(input) != -1:
        return (abcd[(abcd.find(input)+rotate)%26])
    elif abcd_caps.find(input) != -1:
        return (abcd_caps[(abcd_caps.find(input)+rotate)%26])
    else:
        return input

def caesarCipher(s, k):
    input_str = s
    shift = k
    result = ""
    for x in range(0, len(input_str)):
        result = result + (replace_char(input_str[x], shift))
    return(result)


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
