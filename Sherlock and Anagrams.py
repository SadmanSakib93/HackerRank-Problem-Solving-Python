#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagramDict = {}
    count = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i+1):
            current = str(sorted(s[j:j+i]))
            if (current not in anagramDict):
                anagramDict[current] = 1
            else:
                count += anagramDict[current]
                anagramDict[current] += 1
    return (count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
