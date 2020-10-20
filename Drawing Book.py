#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if((n%2==1 and (n-p)==1) or ((p==n or p==1))):
        return 0
    shortestDistance=0
    count=0
    if(abs(p-1)>=abs(n-p)):
        shortestDistance=abs(n-p)
        for i in range(p, n, 2):
            count+=1
        print("count", count)
        if(n%2==1 and p%2==0):
            count-=1
        print("count", count)
    else:
        shortestDistance=abs(p-1)
        for i in range(1, p, 2):
            count+=1
    print("shortestDistance", shortestDistance,"count", count)

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
