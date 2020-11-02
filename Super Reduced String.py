#!/bin/python3

import math
import os
import random
import re
import sys

def removeAt(i, s):
    return s[:i] + s[i+1:]

# Complete the superReducedString function below.
def superReducedString(s):
    print(s)
    currLen=len(s)
    i=0
    while(i<currLen-1):
        # print("currLen", currLen)
        # print( "i", i, "initial", s)
        if(s[i]==s[i+1]):
            s=removeAt(i, s)
            s=removeAt(i, s)
            # print( "i", i, "after removed", s)
            currLen=len(s)
            i=0
        else:
            i+=1
    
    if(len(s)!=0):
        return(s)
    else:
        return("Empty String")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
