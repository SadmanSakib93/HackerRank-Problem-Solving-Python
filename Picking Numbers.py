#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    print(a)
    maxCounter=0
    for i in range(0, len(a)):
        counter=0
        for j in range(i, len(a)-1):
            print(a[j], a[j+1])
            if((a[j]-a[j+1]==-1 or a[j]-a[j+1]==0) and (a[i]-a[j+1]==-1 or a[i]-a[j+1]==0)):
                counter+=1
            else:
                break
        if(counter>maxCounter):
            maxCounter=counter
    print(maxCounter)
    return maxCounter+1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
