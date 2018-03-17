# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import sys

def hackerrankInString(s):
    abcd="abcdefghijklmnopqrstuvwxyz"
    abcd_caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dummy=0
    for x in range (0,len(abcd)):
        if (s.find(abcd[x]) != -1 or s.find(abcd_caps[x]) != -1):
           dummy=dummy+1
        else:
            return "not pangram"
    return "pangram"

if __name__ == "__main__":
        s = input().strip()
        result = hackerrankInString(s)
        print(result)