import math
import os
import random
import re
import sys

def get_warn_index(n, m, s):
    warn_index=(m+s)-1
    if(warn_index>n):
        warn_index=warn_index-n
    if(warn_index==0):
        warn_index=n   
    return warn_index

def saveThePrisoner(n, m, s):
    warn_index=-1
    if(m>n):
        m=m%n
    warn_index=get_warn_index(n, m, s)
        
    return warn_index

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(raw_input().strip())
    for t_itr in xrange(t):
        first_multiple_input = raw_input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        s = int(first_multiple_input[2])
        result = saveThePrisoner(n, m, s)
        fptr.write(str(result) + '\n')
    fptr.close()
