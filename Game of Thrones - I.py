#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    if(len(s)==1):
        return 'YES'
    sDict=dict(Counter(s))
    oddFlag=False
    oddCount=0
    for key, value in sDict.items():
        if(value%2!=0):
            oddCount+=1           
            if(oddCount>1):
                oddFlag=True
                break
    if(oddFlag==False):
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
