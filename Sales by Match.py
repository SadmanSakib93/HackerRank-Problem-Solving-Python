#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    results = {value: len(list(ar)) for value, ar in groupby(sorted(ar))}
    print(type(results))
    count=0
    for key, value in results.items():
        count+=value//2
    return (count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
