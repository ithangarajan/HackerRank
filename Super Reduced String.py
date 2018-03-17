import sys

def super_reduced_string(s):
    x=0
    counter =0
    result=""

    for x in range(0,len(s)):
        if (counter<len(s)):
            if counter != len(s)-1:
                if s[counter] == s[counter+1] :
                    counter = counter +2
                else:
                    result = result + s[counter]
                    counter=counter+1
            else:
                result = result + s[counter]
                counter = counter + 1

    return result
s = input().strip()
result="BEGIN"
while (s != result and result !=""):
    if result == "BEGIN":
            result = super_reduced_string(s)
    else:
            s = result
            result = super_reduced_string(s)
if (result==""):
    print ("Empty String")
else:
    print(result)
