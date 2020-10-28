#!/bin/python3

import math
import os
import random
import re
import sys

def countFrequency(my_list): 

   count = {} 
   for i in my_list: 
    count[i] = count.get(i, 0) + 1
   return count 

# Complete the equalizeArray function below.
def equalizeArray(arr):
    arrDict=countFrequency(arr)
    maxValue=max(arrDict.values())
    return len(arr)-maxValue

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
