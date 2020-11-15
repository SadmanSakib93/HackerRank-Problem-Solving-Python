#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    bit32='{:032b}'.format(n)
    print(bit32)
    bit32Inverted=''

    for eachBit in bit32:
        if(eachBit=='0'):
            bit32Inverted+='1'
        else:
            bit32Inverted+='0'
    return (int(bit32Inverted, 2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
