#!/bin/python3

import math
import os
import random
import re
import sys
import operator

# Complete the toys function below.
def toys(w):
    w.sort()
    total=0
    i=0
    j=0
    while(i<len(w)):
        start=w[i]
        end=start+4
        j=end
        while(j>=start):
            if(w[i:].count(j)!=0):
                i=len(w) - operator.indexOf(reversed(w), j) - 1
                total+=1
                break
            j-=1
        i+=1
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
