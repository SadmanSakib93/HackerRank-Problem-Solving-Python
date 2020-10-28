#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    totalCount=0
    if(len(s)==1 and s.count("a")==1):
        totalCount = n
    else:
        baseCount=s.count("a")
        totalCount = baseCount * (n//len(s))
        remaining=(n%len(s))
        remainingCount=s[:remaining].count("a")
        totalCount += remainingCount

    return totalCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
