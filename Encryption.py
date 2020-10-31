#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s.replace(" ", "")
    upperBound=math.ceil(math.sqrt(len(s)))  #col
    lowerBound=math.floor(math.sqrt(len(s))) #row
    if(upperBound*lowerBound<len(s)):
        lowerBound+=1

    result=[]
    indexCount=0
    for i in range(0, lowerBound):
        rowElems=[]
        for j in range(0, upperBound):
            try:
                rowElems.append(s[indexCount])
                indexCount+=1
            except:
                break
        result.append(rowElems)
    
    c=0
    resultStr=''

    print(result)
    for i in range(0, len(result[0])):
        for j in range(0, len(result)):
            try:
                print(result[j][i], end="")
                resultStr+=result[j][i]
            except:
                continue
        resultStr+=" "
        # print("")

    return resultStr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
