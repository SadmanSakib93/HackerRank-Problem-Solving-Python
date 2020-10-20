#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    # print(bill)
    # print(k)
    # print(b)
    total=0
    for i in range(0, len(bill)):
        if(i==k):
            continue
        total+=bill[i]
    # print("total",total)
    if((total//2)==b):
        return "Bon Appetit"
    else:
        return b-(total//2)
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))
