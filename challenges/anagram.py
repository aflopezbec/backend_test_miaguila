#!/bin/python3

import math
import os
import random
import re
import sys
import time

# input: String
# output: Code with the number of concurrences
def alphabetValue(sub1):
    alpabet_sub1 = [0]*26 # 0:a ... 25:z
    for i in range(len(sub1)):
        char_sub1 = ord(sub1[i])-97
        alpabet_sub1[char_sub1] +=1
    return str(alpabet_sub1)

# input: String
# output: number of anagrams found
def countAnagrams(s):  
    len_arr = len(s)
    count = 0 
    for size in range(1,len_arr):
        level_array = {}
        for index in range(len_arr-size+1):
            value_sub_string = alphabetValue(s[index:index+size])
            if value_sub_string in level_array:
                level_array[value_sub_string] += 1
            else:
                level_array[value_sub_string] = 1
            count += level_array[value_sub_string] - 1
    return count

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    return countAnagrams(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
