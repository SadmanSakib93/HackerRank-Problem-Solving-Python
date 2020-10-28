#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    print(c)
    count=0
    i=0
    while(i<len(c)-1):
        print("i",i,"count",count)
        try:
            if(c[i+2]!=1):
                i+=2
            else:
                i+=1
        except:
            i+=1
        count+=1
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
