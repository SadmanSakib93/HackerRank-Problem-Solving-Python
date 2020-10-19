#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plusC=0
    minusC=0
    zeroC=0
    for each in arr:
        if(each<0):
            minusC+=1
        elif(each>0):
            plusC+=1   
        else:
            zeroC+=1  
    # print([plusC/len(arr), minusC/len(arr), zeroC/len(arr)])
    return [plusC/len(arr), minusC/len(arr), zeroC/len(arr)]

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    resArr=plusMinus(arr)
    for each in resArr:
        print(each)
