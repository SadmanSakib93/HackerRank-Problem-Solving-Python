import math
import os
import random
import re
import sys

# x + y + x = sum of array
# 2x+y = sum  of array
# 2x = sum  of array - y

def balancedSums(arr):
    arr_sum=sum(arr)
    remaining=0
    for val in arr:
        if(2*remaining==arr_sum-val):
            return "YES"
        else:
            remaining+=val
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(raw_input().strip())
    for T_itr in xrange(T):
        n = int(raw_input().strip())
        arr = map(int, raw_input().rstrip().split())
        result = balancedSums(arr)
        fptr.write(result + '\n')
    fptr.close()