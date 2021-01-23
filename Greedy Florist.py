#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=False)
    totalCost=0
    for i in range(k):
        totalCost+=c[len(c)-i-1]
        
    remainIndex = len(c)-k-1
    multiplyWith = 2
    while(remainIndex>=0):
        totalCost+=c[remainIndex]*multiplyWith
        remainIndex-=1
        if(remainIndex==len(c)-(k*multiplyWith)-1):
            multiplyWith+=1
        
    return totalCost
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
