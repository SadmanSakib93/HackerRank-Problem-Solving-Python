#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # print(x1,v1,x2,v2)
    message=''
    if((x1>x2 and v1>v2) or (x1<x2 and v1<v2)):
        message="NO"
        # print("NO")
    else:
        travel1=x1
        travel2=x2
        itrThreshold=5000
        i=0
        while(travel1!=travel2 and i<=itrThreshold):
            i+=1
            travel1+=v1
            travel2+=v2
        print("i",i)
        print("travel1",travel1)
        print("travel2",travel2)
        if(travel1==travel2):
            message="YES"
            # print("YES")
        else:
            message="NO"
            # print("NO")
    return message

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
