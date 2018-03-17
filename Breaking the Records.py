#!/bin/python3

import sys

def breakingRecords(score):
    answer=[]
    high=score[0]
    high_count=0
    low=score[0]
    low_count=0
    for x in score:
        if x>high:
            high_count=high_count+1
            high=x
        if x<low:
            low_count=low_count+1
            low=x
    answer.append(high_count)
    answer.append(low_count)
    return answer

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))