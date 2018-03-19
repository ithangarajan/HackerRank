#!/bin/python3

import sys

def climbingLeaderboard(scores, alice):
    rank=1
    rank_list=[1]
    answer=[]
    for x in range(1,len(scores)):
        if scores[x]==scores[x-1]:
            rank_list.append(rank_list[x-1])
        else:
            rank=rank+1
            rank_list.append(rank)
    for x in range(0,len(alice)):
        flag=0
        for y in range(0,len(scores)):
            if (alice[x]>=scores[y]):
                answer.append(rank_list[y])
                flag=1
                break
        if flag==0:
            if alice[x]==scores[-1]:
                answer.append(rank_list[-1])
            else:
                answer.append(rank_list[-1]+1)
    return answer


if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))
