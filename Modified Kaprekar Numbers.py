#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    results=[]
    for originalNum in range(p, q+1):
        originalLength=len(str(originalNum))

        squareNum=pow(originalNum,2)
        squareNumStr=str(squareNum)
        if(len(squareNumStr)%2!=0):
            firstNum, secondNum = squareNumStr[:len(squareNumStr)-(len(squareNumStr)-originalLength)-1], squareNumStr[len(squareNumStr)-originalLength:]
        else:
            firstNum, secondNum = squareNumStr[:len(squareNumStr)//2], squareNumStr[len(squareNumStr)//2:]
        if(len(firstNum)==0):
            firstNum=0
        else:
            firstNum=int(firstNum)
        if(len(secondNum)==0):
            secondNum=0
        else:
            secondNum=int(secondNum)
        sumOfTwo=firstNum+secondNum

        if(sumOfTwo==originalNum):
            results.append(originalNum)
        
    if(len(results)>0):
        for each in results:
            print(each, end=" ")
    else:
        print("INVALID RANGE")
    


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
