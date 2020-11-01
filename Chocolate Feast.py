#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    totalEaten=0
    totalEaten=n//c
    wrappersLeft=totalEaten
    print("totalEaten1",totalEaten)

    # 6 2 2

    prev=totalEaten
    while(True):
        newEaten=wrappersLeft//m
        totalEaten+=newEaten
        if(totalEaten==prev):
            break
        prev=totalEaten
        print("totalEaten",totalEaten)
        wrappersLeft=newEaten+wrappersLeft%m

    return totalEaten
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
