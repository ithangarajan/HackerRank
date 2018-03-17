import sys

def camelcase(s):
    counter =0
    for x in range(0,len(s)-1):
        if (s[x].isupper()):
            counter = counter+1
    return counter+1
if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)