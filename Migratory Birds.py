import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    countDict=dict(Counter(arr))
    print(countDict)
    maxVal=0
    maxKey=0
    for key, val in countDict.items():
        if(val>maxVal or (val==maxVal and maxKey>key)):
            maxVal=val
            maxKey=key
    return (maxKey)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
