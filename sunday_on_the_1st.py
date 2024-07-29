#!/bin/python3

import math
import os
import random
import re
import sys
import datetime


#
# Complete the 'numSundaysOnFirst' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER year as parameter.
#

def numSundaysOnFirst(year):
    sundays_count = 0
    for month in range(1, 13):
        if datetime.datetime(year, month, 1).weekday() == 6:
            sundays_count += 1
    return sundays_count

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = numSundaysOnFirst(year)

    fptr.write(str(result) + '\n')

    fptr.close()
