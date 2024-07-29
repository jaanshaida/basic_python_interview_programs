# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
    result = False
    prev = ''
    for value in nums:
        if value == prev and value == 2:
            result = True
            break
        prev = value
    return result

# Test cases
print(has22([1, 3, 3]))  # Output: True
print(has22([1, 2, 1, 2]))  # Output: False
print(has22([2, 1, 2]))  # Output: False
print(has22([2, 2, 1, 2]))  # Output: True
print(has22([1, 2, 3, 4, 2]))  # Output: False
print(has22([2, 2]))  # Output: True
print(has22([]))  # Output: False

import array

my_arr = array.array('i',[1,2,3,4])

my_lst = [1,2,3,4]

import sys
print(sys.getsizeof(my_arr))
print(sys.getsizeof(my_lst))