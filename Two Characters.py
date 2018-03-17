#!/bin/python3

import sys

def check_char (str,check):
    for x in range(len(str)):
        if check == str[x]:
            return 0
    return 1

def list_of_char(mystr):
    resultstr=""
    for x in range(len(mystr)):
        if check_char(resultstr,mystr[x]):
            resultstr=resultstr+mystr[x]
    return (resultstr)

def form_new_string (mystr,x,y):
    new_str=mystr
    for c in range(len(mystr)):
        #print ("for",mystr,mystr[c],x,y)
        if ((mystr[c] == x or mystr[c] == y)):
            new_str=new_str.replace(mystr[c],"")
    return new_str
def valid_str(s):
    for x in range(0,len(s)-1):
        if (s[x] == s[x+1]):
            return 0
    return 1



def twoCharaters(s):
    inputstr = s
    result = list_of_char(inputstr)
    answer = ""
    answer_length = 0
    for x in range(len(result)):
        for y in range(len(result)):
            # print ("invoking",inputstr,result[x],result[y])
            if (result[x] != result[y]):
                new_string = form_new_string(inputstr, result[x], result[y])
                if valid_str(new_string):
                    if answer_length < len(new_string):
                        answer = new_string
    return(len(answer))


if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)