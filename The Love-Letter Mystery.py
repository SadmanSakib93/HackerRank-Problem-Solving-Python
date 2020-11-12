#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    asciiStr=[ord(c) for c in s]
    result=0
    for i in range(0, len(asciiStr)):
        result += abs(asciiStr[i]-asciiStr[len(asciiStr)-i-1])
    return (result//2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
