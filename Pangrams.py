#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the pangrams function below.
def pangrams(s):
    result='pangram'
    if(len(s)<26):
        result='not pangram'
    else:
        alphabets = string.ascii_lowercase
        s=s.lower()
        for eachAlph in alphabets:
            print(eachAlph, " in : ", eachAlph in s)
            if(eachAlph not in s):
                result='not pangram'
                break
    print(result)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
