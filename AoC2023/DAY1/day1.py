# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 06:33:35 2023
@author: matus

DAY1: Trebuchet
----------------
each line calibration value 
    = first digit & last digit == 2 digit number
    (if just one digit, both first and last)
Sum of all calibration values
"""
from numpy import array, isin
import re

#%% Part 2 - what the fuck
def find_max_min_nested_list(nested_list):
    max_val = max(nested_list[0])
    min_val = min(nested_list[0])
    min_ind, max_ind = 0,0
    for i, l in enumerate(nested_list):
        if max(nested_list[i]) > max_val:
            max_val = max(nested_list[i])
            max_ind = i
            
        if min(nested_list[i]) < min_val:
            min_val = min(nested_list[i])
            min_ind = i
            
    return min_ind, max_ind

num_str = list(map(lambda x: str(x), list(range(10))))
spelled_out = ['zero','one','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums_dict = {spelled:num for spelled, num in zip(spelled_out, num_str)} # dictionary comprehension
num_str += spelled_out

cal_vals = dict() #empty dictionary

with open('day1_input.txt', 'r') as mixed_input:
    # Loop through lines
    for i, line in enumerate(mixed_input):
        # Finding substrings
        where_nums, what_nums, ind = [],[], 0
        
        for n in num_str:
            if n in line:
                # only store end index of number occurences (highest end index = last, lowest end index = first)
                where_n = [m.span()[1] for m in re.finditer(n,line)]
                # print(n, *where_n)
                # Which nth value n is from all values in num_str
                # is outer key, inner key is the actual number and value is its index
                where_nums.append(where_n) , what_nums.append(n)
                ind += 1
                
        firsts_ind, lasts_ind = find_max_min_nested_list(where_nums)      
        first, last = what_nums[firsts_ind], what_nums[lasts_ind]

        try:
            if first in list(nums_dict.keys()):
                first = nums_dict[first]
            
            if last in list(nums_dict.keys()):
                last = nums_dict[last]
            
            cal_vals[i] = int(first+last)
            
        except ValueError:
            breakpoint()
        
    print("Part 2 result:", sum(cal_vals.values()))




#%% Part 1 - EASY
num_str = list(map(lambda x: str(x), list(range(10))))
cal_vals = {0:0}

with open('day1_input.txt', 'r') as mixed_input:
    for i, line in enumerate(mixed_input):
        all_letters = array(list(line))
        
        nums_in_line = all_letters[isin(all_letters, num_str)]
        
        if len(nums_in_line) > 1:
            first, last = nums_in_line[0], nums_in_line[-1]
            
        elif len(nums_in_line) == 1:
            first, last = nums_in_line[0],nums_in_line[0]
        
        else:
            continue

        try:
            cal_vals[i] = int(first+last)
        except ValueError:
            breakpoint()
        
    print("Part 1 result:", sum(cal_vals.values()))
        