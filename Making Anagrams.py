#!/bin/python3

import math
import os
import random
import re
import sys
import string
from collections import Counter

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    allAlphs=list(string.ascii_lowercase)
    s1CountList=[]
    s2CountList=[]
    s1Dict=dict(Counter(s1))
    s2Dict=dict(Counter(s2))

    for eachAlph in allAlphs:
        s1CountList.append(s1.count(eachAlph))
        s2CountList.append(s2.count(eachAlph))

    count=0
    for i in range(0, len(s1CountList)):
        count+=abs(s1CountList[i]-s2CountList[i])
    
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
