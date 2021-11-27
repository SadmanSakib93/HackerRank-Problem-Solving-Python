import math
import os
import random
import re
import sys
import itertools

# Check if a string is valid (i.e., two length and having alternate chars)
def is_valid(string_value):
    valid_flag=True
    unique_chars=set(string_value)
    if(len(unique_chars)==2):
        prev_char=string_value[0]
        for i in range(1, len(string_value)):
            if(prev_char==string_value[i]):
                valid_flag=False
                break
            prev_char=string_value[i]
    else:
        valid_flag=False
    return valid_flag
            
def alternate(s):
    char_allow=2
    result=0
    unique_chars=set(s)
    if(len(unique_chars)>=char_allow):
        all_permutations=(list(itertools.permutations(unique_chars, char_allow)))
        for permutation in all_permutations:
            temp = [x for x in s if x in permutation]
            valid_flag=is_valid(temp)
            if(valid_flag and len(temp)>result):
                result=len(temp)
    
    return result
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(raw_input().strip())

    s = raw_input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()