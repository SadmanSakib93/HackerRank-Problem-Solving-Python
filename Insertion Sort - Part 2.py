#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        for i in range(len(arr)): 
            print (arr[i], end=" ") 
        print("")
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
