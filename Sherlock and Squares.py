#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    #Iterative solution -> timeout problem
    # count=0
    # for i in range(a, b+1):
    #     sqrVal=math.sqrt(i)
    #     # print(i, type(sqrVal))
    #     if(sqrVal.is_integer()):
    #         count+=1
    # return (count)

    #Another solution!
    return (math.floor(math.sqrt(b))-math.ceil(math.sqrt(a))+1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
