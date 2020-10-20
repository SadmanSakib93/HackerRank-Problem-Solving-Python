#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount=0
    count=0
    for each in range(len(s)):
        if(s[each]=='D'):
            count-=1
        elif(s[each]=='U'):
            count+=1
        if(s[each]=='U' and count==0):
            valleyCount+=1
    return valleyCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
