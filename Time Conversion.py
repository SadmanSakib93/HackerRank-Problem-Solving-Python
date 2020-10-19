#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    splittedString=s[len(s)-2]+s[len(s)-1]
    hourMinSec=s.split(":")
    newHour=''
    if(splittedString=="AM"):
        if(hourMinSec[0]=="12"):
            newHour="00"
        else:
            newHour=hourMinSec[0]
    else:
        if(int(hourMinSec[0])!=12):
            newHour=12+int(hourMinSec[0])
        else:
            newHour=12
    return (str(newHour)+":"+hourMinSec[1]+":"+hourMinSec[2][:2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
