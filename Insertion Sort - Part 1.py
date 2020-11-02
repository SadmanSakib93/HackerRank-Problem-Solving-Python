#!/bin/python3

import math
import os
import random
import re
import sys

def display(arr):
    for each in range(0, len(arr)):
        if(each!=len(arr)-1):
            print(arr[each], end=" ")
        else:
            print(arr[each], end="")
    print("")
# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    arrBkp=arr.copy()
    # print(arr)
    result=[]
    num=arr[len(arr)-1]
    arr[len(arr)-1]=arr[len(arr)-2]
    arrTemp=arr.copy()

    for i in range(len(arrTemp)-1, -1, -1):
        
        # if(num>=arrTemp[i-1]):
        #     continue
        if(num<arrTemp[i]):
            arrTemp[i]=arrTemp[i-1]
        elif(num>=arrTemp[i]):
            arrTemp[i+1]=num
            break
        # display(arrTemp)
        result.append(arrTemp.copy())
    # display(arrTemp)
    arrBkp.sort()
    result.append(arrBkp)

    del result[len(result)-2]

    for each in result:
        display(each)

        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
