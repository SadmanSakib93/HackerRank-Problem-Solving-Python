#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    k=k%26
    lowerAplhs=string.ascii_lowercase
    upperAplhs=string.ascii_uppercase
    resultString=''
    for eachChar in s:
        if(eachChar in lowerAplhs):
            currIndex=lowerAplhs.index(eachChar)
            newIndex=0
            if(currIndex+k<len(lowerAplhs)):
                newIndex=currIndex+k
            else:
                newIndex=currIndex+k-len(lowerAplhs)
            resultString+=lowerAplhs[newIndex]
        elif(eachChar in upperAplhs):
            currIndex=upperAplhs.index(eachChar)
            newIndex=0
            if(currIndex+k<len(upperAplhs)):
                newIndex=currIndex+k
            else:
                newIndex=currIndex+k-len(upperAplhs)
            resultString+=upperAplhs[newIndex]
        else:
            resultString+=eachChar
    return (resultString)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
