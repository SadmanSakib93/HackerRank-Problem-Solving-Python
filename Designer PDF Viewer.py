#!/bin/python3

import math
import os
import random
import re
import string
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    smallAlphabets=list(string.ascii_lowercase)
    wordValueList=[]
    for eachAlphabet in word:
        alphaIndex=smallAlphabets.index(eachAlphabet)
        wordValueList.append(h[alphaIndex])
    return len(word)*max(wordValueList)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
