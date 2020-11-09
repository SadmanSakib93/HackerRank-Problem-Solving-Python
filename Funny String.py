#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    result=''
    sRev=s[::-1]
    sASCII=[ord(c) for c in s]
    sRevASCII=[ord(c) for c in sRev]

    sAdjDiff=list()
    sRevAdjDiff=list()
    for i in range(0, len(sASCII)-1):
        sAdjDiff.append(abs(sASCII[i]-sASCII[i+1]))
    for i in range(0, len(sRevASCII)-1):
        sRevAdjDiff.append(abs(sRevASCII[i]-sRevASCII[i+1]))

    if(sAdjDiff==sRevAdjDiff):
        result='Funny'
    else:
        result='Not Funny'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
