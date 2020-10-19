import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    joinedList = a + b
    minRange=min(joinedList)
    maxRange=max(joinedList)
    print(minRange, maxRange)
    result=0
    
    for num in range(minRange, maxRange+1):
        trueFlag=True
        for i in a:
            # print(num%i)
            if(num%i!=0):
                trueFlag=False
                break
        if(trueFlag==True):
            for j in b:
                # print(j%num)
                if(j%num!=0):
                    trueFlag=False
                    break   
        if(trueFlag==True):
            result+=1
            print(num)
    return result             
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()