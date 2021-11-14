#!/bin/python3

import os
import re

def check_validity(bot_energy, arr):
    for height in arr:
        delta=(bot_energy-height)
        bot_energy+=delta
        if(bot_energy<0):
            return False
    return True

def chiefHopper(arr):
    for bot_energy in range(0, max(arr)+1):
        validity=check_validity(bot_energy, arr)
        print(bot_energy, validity)
        if(validity):
            break
    return bot_energy
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = chiefHopper(arr)
    fptr.write(str(result) + '\n')
    fptr.close()