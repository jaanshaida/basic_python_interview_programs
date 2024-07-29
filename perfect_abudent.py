#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'classify' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER number as parameter.
#


def classify(num):
    # Write your code here
    div_sum = sum(x for x in range(1, num) if num % x == 0)
    kind = ""
    if div_sum < num:
        kind = "Deficient"
    elif div_sum > num:
        kind = "Abundant"
    else:
        kind = "Perfect"
    print("{} is a {} number".format(num, kind))
    return kind


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    number = int(input().strip())

    result = classify(number)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
