#!/bin/python3

import math
import os
import random
import re
import itertools
import sys

n = int(input())
arr = list(map(int,input().split()))
sortedarr = sorted(arr)
a = []
subarray = []
counter = 0
for i in range(n):
    if arr[i] != sortedarr[i] :
        counter += 1
        a.append(i+1)
if counter == 2:
    print("yes")
    print("swap", a[0],a[1],sep = " ")
else:       
    for i in range(n):
        if arr[i] == sortedarr[i] :
            None
        else:
            subarray.append(arr[i])
    if subarray == sorted(subarray,reverse = True):
        print("yes")
        print("reverse", arr.index(subarray[0])+1,arr.index(subarray[-1])+1,sep=" ")
    else:
        print("no")
