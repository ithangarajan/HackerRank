#!/bin/python3

import sys

def climbingLeaderboard(scores, alice):
    rank_list=[1]
    rank=1
    counter=1
    while (True):
        if scores[counter-1] == scores[counter]:
            rank_list.append(rank)
            counter = counter + 1
        else:
            rank_list.append(rank)
            rank=rank+1
            counter=counter+1



if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    result = climbingLeaderboard(scores, alice)
    print ("\n".join(map(str, result)))
