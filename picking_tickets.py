#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxTickets function below.
def maxTickets(tickets):
    tickets.sort()
    max_length = 1
    current_length = 1
    for i in range(1, len(tickets)):
        if tickets[i] - tickets[i - 1] <= 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1
    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tickets_count = int(input().strip())

    tickets = []

    for _ in range(tickets_count):
        tickets_item = int(input().strip())
        tickets.append(tickets_item)

    res = maxTickets(tickets)

    fptr.write(str(res) + '\n')

    fptr.close()
