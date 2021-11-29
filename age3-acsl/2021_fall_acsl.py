#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findTime' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. CHARACTER c1
#  2. CHARACTER c2
#  3. CHARACTER c3
#  4. CHARACTER c4
#  5. CHARACTER c5
#
def fibonacci(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)
def findTime(c1, c2, c3, c4, c5):
    # Write your code here
    hour = 0
    minute = 0
    validcolors = ['R','G','B','W']
    listofcolors = [c1,c2,c3,c4,c5]
    for i in listofcolors:
        if i not in validcolors:
            print('Hey, that is not valid')
            exit(-1)
    for i in range(len(listofcolors)):
        if listofcolors[i] == 'R':
            hour += fibonacci(i+1)
        elif listofcolors[i] == 'G':
            minute += fibonacci(i+1)
        elif listofcolors[i] == 'B':
            hour += fibonacci(i+1)
            minute +=  fibonacci(i+1)
        elif listofcolors[i] == 'W':
            pass
        else:
            pass
    minute = minute * 5
    if minute >= 60:
        while minute >= 60:
            minute = minute - 60
            hour += 1
    if len(str(hour)) == 1:
        hour = '0' + str(hour)
    if len(str(minute)) == 1:
        minute = '0' + str(minute)

    return f'{hour}:{minute}'


if __name__ == '__main__':
    print(findTime('B','B','B','B','B'))
#1 digit hour
#1 digit minute
