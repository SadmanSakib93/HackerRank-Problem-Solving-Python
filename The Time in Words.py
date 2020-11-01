#!/bin/python3

import math
import os
import random
import re
import sys

numbersWords=["zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"]

# Complete the timeInWords function below.
def timeInWords(h, m):
    output=''
    hourWord=numbersWords[h]

    if(m==0):
        output=str(hourWord)+" o' clock"
    elif(m==1):
        output='one minute past '+str(hourWord)
    elif(m==15):
        output='quarter past '+str(hourWord)
    elif(m==30):
        output='half past '+str(numbersWords[h])
    elif(m==45):
        output='quarter to '+str(numbersWords[h+1])
    elif(m<30):
        minWord=numbersWords[m]
        output=str(minWord)+' minutes past '+str(hourWord)
    elif(m>30):
        minWord=numbersWords[60-m]
        output=str(minWord)+' minutes to '+str(numbersWords[h+1])
    else:
        output='N/A'
    # print(hourWord)
    # print(minWord)
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
