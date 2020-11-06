#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    splitString=[]
    for i in range(0, len(s), 3):
        splitString.append(s[i : i + 3])
    # print(splitString)

    count=0
    for each in splitString:
        if(each[0]!='S'):
            count+=1
        if(each[1]!='O'):
            count+=1
        if(each[2]!='S'):
            count+=1 
    return (count)       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
