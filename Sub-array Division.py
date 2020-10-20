import math
import os
import random
import re
import sys
import itertools

# Complete the birthday function below.
def birthday(s, d, m):
    count=0
    if(len(s)==1):
        return 1
    for i in range(0, len(s)):
        tempSum=0
        print(s[i:i+d])
        for j in range(i, i+m):
            try:
                tempSum+=s[j]
            except:
                tempSum=tempSum
        if(tempSum==d):
            count+=1


    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
