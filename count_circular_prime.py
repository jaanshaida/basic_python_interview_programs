#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countCircularPrimes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER number as parameter.
#
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_rotations(n):
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        rotations.append(int(rotated))
    return rotations

def is_circular_prime(n):
    rotations = get_rotations(n)
    return all(is_prime(rotation) for rotation in rotations)

def countCircularPrimes(number):
    count = 0
    for n in range(2, number + 1):
        if is_circular_prime(n):
            count += 1
    return count
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    number = int(input().strip())

    result = countCircularPrimes(number)

    fptr.write(str(result) + '\n')

    fptr.close()
