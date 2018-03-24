#!/bin/python3

import sys

def designerPdfViewer(h, word):
    letters="abcdefghijklmnopqrstuvwxyz"
    maxHeight=0
    counter=0
    while (counter<len(word)):
        if maxHeight<h[letters.find(word[counter])]:
            maxHeight=h[letters.find(word[counter])]
        counter=counter+1
    return maxHeight*len(word)

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
