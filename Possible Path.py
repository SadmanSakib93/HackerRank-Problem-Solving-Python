#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. LONG_INTEGER a
#  2. LONG_INTEGER b
#  3. LONG_INTEGER x
#  4. LONG_INTEGER y
#

def solve(a, b, x, y):
    # Write your code here
    result_flag = 'NO'
    if(math.gcd(a, b) == math.gcd(x, y)):
        result_flag = 'YES'
        
    return str(result_flag)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        x = int(first_multiple_input[2])

        y = int(first_multiple_input[3])

        result = solve(a, b, x, y)

        fptr.write(result + '\n')

    fptr.close()
