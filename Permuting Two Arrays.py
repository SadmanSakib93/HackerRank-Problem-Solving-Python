#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoArrays function below.
def twoArrays(k, A, B):
    print(A, B)
    A_sorted=sorted(A)
    B_sorted=sorted(B, reverse=True)
    print(A_sorted, B_sorted)

    flag=True
    for i in range(0, len(A_sorted)):
        if(A_sorted[i]+B_sorted[i]<k):
            flag=False
            break
    print(flag)
    if(flag==True):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
