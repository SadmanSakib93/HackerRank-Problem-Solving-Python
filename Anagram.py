#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the anagram function below.
def anagram(s):
    if(len(s)%2!=0):
        return -1
    firstStr, secondStr = s[:len(s)//2], s[len(s)//2:]
    allAlphabets = list(string.ascii_lowercase)
    firstAlphCount=[]
    secondAlphCount=[]
    for eachAlph in allAlphabets:
        firstAlphCount.append(firstStr.count(eachAlph))
        secondAlphCount.append(secondStr.count(eachAlph))

    count=0
    for i in range(0, len(firstAlphCount)):
        if(firstAlphCount[i]>secondAlphCount[i]):
            count+=(firstAlphCount[i]-secondAlphCount[i])
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
