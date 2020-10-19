#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        c=0
        for j in range(n-i-1):
            c+=1
            print(' ', end ="")
        for k in range(n-c):
            print('#', end ="")
        print("")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
