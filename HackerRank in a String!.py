#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    print(s)
    result=''
    charsList=['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    lastIndex=-1
    foundCount=0
    for eachChar in charsList:
        # print(eachChar," searching in ", lastIndex+1, s[lastIndex+1]," to ", len(s)-1, s[len(s)-1])
        for i in range(lastIndex+1, len(s)):
            if(s[i]==eachChar):
                # print(eachChar," found at ",i)
                lastIndex=i
                foundCount+=1
                break
        # lastIndex=currIndex
        # print(eachChar,currIndex,lastIndex)
    print("foundCount",foundCount)
    if(foundCount==len(charsList)):
        result='YES'
    else:
        result='NO'   
    return (result)
        

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
