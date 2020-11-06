#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the separateNumbers function below.
def separateNumbers(s):
    # print(s)
    if(len(s)<=1 or (len(s)==2 and s[0]!=str(int(s[1])+1))):
        return "NO"

    for tryNumber in range(1, (len(s)//2)+1):
        beautifulString=''
        firstStr=s[:tryNumber]
        beautifulString+=firstStr
        nextStr=firstStr
        for i in range(0, len(s)//len(firstStr)):
            nextStr=str(int(nextStr)+1)
            beautifulString+=nextStr
            if(len(beautifulString)>=len(s)):
                break
        # print("beautifulString",tryNumber,len(s), len(beautifulString), beautifulString)
        # print("SPLITTED:::beautifulString", tryNumber, beautifulString[:len(s)])
        if(beautifulString==s):
            return "YES "+firstStr
            break
    return "NO"
    


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))
