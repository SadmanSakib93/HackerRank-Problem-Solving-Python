#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    print(arr,m)
    firstIndex, secondIndex=0, 0
    for i in range(0, len(arr)):
        if(arr[i]>m):
            continue
        for j in range(i, len(arr)):
            if(arr[j]>m):
                continue
            if(i!=j and arr[i]+arr[j]==m):
                firstIndex=i+1
                secondIndex=j+1
    return (firstIndex, secondIndex)
                           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
