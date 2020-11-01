#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    totalCost=0
    totalBuy=0
    if(p>s):
        return 0
    elif(p==s):
        return 1
    while(True):
        if(totalCost+p<=s):
            totalCost+=p
            totalBuy+=1
        else:
            break
        
        if(p-d>m):
            p-=d
        else:
            p=m

    return totalBuy

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
