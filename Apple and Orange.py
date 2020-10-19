#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # print(s,t,a,b,apples,oranges)
    countApples=0
    countOranges=0
    # print("APPLES")
    for each in apples:
        fallLocation=a+each
        if(fallLocation>=s and fallLocation<=t):
            countApples+=1
        # print(fallLocation)
    # print("ORANGES")
    for each in oranges:
        fallLocation=b+each
        if(fallLocation>=s and fallLocation<=t):
            countOranges+=1
        # print(fallLocation)
    print(countApples)
    print(countOranges)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
