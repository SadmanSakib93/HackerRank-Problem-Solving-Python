#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    print(password, n)

    numFlag, lowerFlag, upeerFlag, specialFlag =  False, False, False, False
    conditionsOK=0
    addRequired=0
    for eachChar in password:
        if(eachChar in numbers and numFlag==False):
            conditionsOK+=1
            numFlag=True
        if(eachChar in lower_case and lowerFlag==False):
            conditionsOK+=1
            lowerFlag=True
        if(eachChar in upper_case and upeerFlag==False):
            conditionsOK+=1
            upeerFlag=True
        if(eachChar in special_characters and specialFlag==False):
            conditionsOK+=1
            specialFlag=True

    if(conditionsOK!=4):
        addRequired+=4-conditionsOK
    if(addRequired+n<6):
        addRequired+=6-(addRequired+n)

    return addRequired
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
