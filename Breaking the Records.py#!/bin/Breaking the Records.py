import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    # print(scores)
    minC=0
    maxC=0
    minV=scores[0]
    maxV=scores[0]
    for index in range(1, len(scores)):
        if(scores[index]>maxV):
            maxC+=1
            maxV=scores[index]
        if(scores[index]<minV):
            minC+=1
            minV=scores[index]
    return maxC, minC
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
