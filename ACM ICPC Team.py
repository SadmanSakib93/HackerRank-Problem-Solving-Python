#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
import itertools

# Complete the acmTeam function below.
def acmTeam(topic):
    topicLengthList=list(range(0, len(topic)))
    topicPermutation = list(itertools.combinations(topicLengthList, 2))
    topicPermutationCount=[]
    for each in topicPermutation:
        sumTwoStr=str(int(topic[each[0]])+int(topic[each[1]]))
        topicPermutationCount.append(len(sumTwoStr)-sumTwoStr.count('0'))
    maxVal=max(topicPermutationCount)
    maxValCount=topicPermutationCount.count(maxVal)
    return (maxVal, maxValCount)

    # --- ANOTHER SOLUTION ---
    # topicLengthList=list(range(0, len(topic)))
    # topicPermutation = list(itertools.combinations(topicLengthList, 2))
    # topicPermutationCount=[]
    # for each in topicPermutation:
    #     count=0
    #     for i in range(0, len(topic[0])):
    #         if(topic[each[0]][i]=='1' or topic[each[1]][i]=='1'):
    #             count+=1
    #     topicPermutationCount.append(count)
    # print("topicPermutationCount",topicPermutationCount)
    # maxVal=max(topicPermutationCount)
    # maxValCount=topicPermutationCount.count(maxVal)
    # return (maxVal, maxValCount)
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
