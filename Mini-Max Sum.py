#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    maxIndex = arr.index(max(arr))
    minIndex = arr.index(min(arr))
    maxSum=minSum=0
    for eachValIndex in range(len(arr)):
        if(maxIndex!=eachValIndex):
            maxSum+=arr[eachValIndex]
        if(minIndex!=eachValIndex):
            minSum+=arr[eachValIndex]
    return maxSum, minSum

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    res=miniMaxSum(arr)

    for each in res:
        print(each, end=' ')
