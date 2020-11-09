#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    occurances=[i for i in range(len(b)) if b.startswith('010', i)] 
    print(occurances)
    
    if(len(occurances)==0):
        return 0
    else:
        res=1
        lastChanged=0
        for i in range(1, len(occurances)):
            if(abs(occurances[lastChanged]-occurances[i])>=3):
                print("Changed")
                lastChanged=i
                res+=1
        return (res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
