#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    result='NO'
    allAlphabets = list(string.ascii_lowercase)
    firstAlphCount=[]
    secondAlphCount=[]
    for eachAlph in allAlphabets:
        firstAlphCount.append(s1.count(eachAlph))
        secondAlphCount.append(s2.count(eachAlph))
    
    for i in range(0, len(firstAlphCount)):
        if(firstAlphCount[i]>0 and secondAlphCount[i]>0):
            result='YES'
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
