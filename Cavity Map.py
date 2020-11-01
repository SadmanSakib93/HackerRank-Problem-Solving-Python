#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    row, col = len(grid[0]), len(grid)
    # print(row, col)
    if(row<=2 or col<=2):
        return grid
    resultGrid=grid.copy()
        
    for i in range(1, row-1):
        convertedList=list(resultGrid[i])
        for j in range(1, col-1):
            # print("grid[i][j]",grid[i][j])
            if((grid[i][j]>grid[i-1][j]) and (grid[i][j]>grid[i+1][j]) and (grid[i][j]>grid[i][j-1]) and (grid[i][j]>grid[i][j+1])):
                convertedList[j]="X"
        convertedStr = ''.join(convertedList)
        # print("convertedStr",convertedStr)
        resultGrid[i]=convertedStr
    return resultGrid


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
