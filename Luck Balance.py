#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key=lambda x: x[0], reverse=True)
    luckTotalVal, luckTotalCount = 0, k
    for each in contests:
        if(each[1]==1 and luckTotalCount>0):
            luckTotalCount-=1
            luckTotalVal+=each[0]
        elif(each[1]==0):
            luckTotalVal+=each[0]        
        elif(each[1]==1 and luckTotalCount==0):
            luckTotalVal-=each[0]
    return luckTotalVal
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
