#!/bin/python3

import math
import os
import random
import re
import sys
import string
from collections import Counter 

allCaps=string.ascii_uppercase
def check_HLB_condition(arr):
    if(len(arr)==1 and arr[0]!='_'):
        return False
    for i in range(len(arr)):
        if(arr[i] in allCaps):
            if(i==0):
                if(arr[i]!=arr[i+1]):
                    return False
            elif(i==len(arr)-1):
                if(arr[i]!=arr[i-1]):
                    return False
            else:
                if(arr[i]!=arr[i+1] and arr[i]!=arr[i-1]):
                    return False
    return True
# Complete the happyLadybugs function below.
def happyLadybugs(b):
    result=True
    if("_" in b):
        resultDict = dict(Counter(b))
        for key, value in resultDict.items():
            if(key!='_' and value==1):
                result=False 
                break
    else:
        result=check_HLB_condition(b)
    
    if(result==True):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
