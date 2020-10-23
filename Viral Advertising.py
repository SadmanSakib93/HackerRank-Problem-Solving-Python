#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    # print(n)
    shared=5
    liked=0
    totalLiked=0
    for i in range(0, n):
        liked=shared//2
        totalLiked+=liked
        shared=0
        # for j in range(0, liked):
        #     shared+=3
        shared=(liked*3)
        # print("shared",shared,"liked",liked,"total",totalLiked)

    return totalLiked


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
