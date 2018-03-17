
import sys

def marsExploration(s):
    number_of_code = int (len(s)/3);
    counter =0
    error=0
    for x in range (0,number_of_code):
        if (s[counter]=="S" and s[counter+1]=="O" and s[counter+2]=="S"):
            counter=counter+3
        else:
            if s[counter]!="S":
                error=error+1
            if s[counter+1]!="O":
                error=error+1
            if s[counter+2]!="S":
                error=error+1
            counter=counter+3
    return error
if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
