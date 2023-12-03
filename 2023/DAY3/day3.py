# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 06:00:27 2023

@author: matus

DAY3

Gear Ratios
-------------

figure out which engine part is missing

engine schematic = visual rep of engine

any number adjacent to symbol 
(even diagonally, +- 0 & 1 index 
 on previous and subsequent line)
== 'part number' to include in sum

. NOT symbol

Part1 - Sum of ALL part numbers in engine schematic
"""
import re
from numpy import array, unique, isin, where

# PART 1 ??????
engine = []
str_engine = []

numbers_str = list(map(lambda x: str(x), list(range(1000))))
where_nums = []

with open ('day3_input.txt', 'r') as engine_schematic:
    for i, lines in enumerate(engine_schematic):
        line = lines[:-1] #drops '\n'
        
        engine.append(array(list(line)))
        str_engine.append(line)
        
        line_nums = []
        for n in numbers_str:
            if n in line:
                # pettern = number preceded and followed by any non-digit character == \D
                # or start of line ^ or end of line or string $
                pattern = f'(^|\D)({n})(\D|$)'
                line_num = [m.span(0)  for m in re.finditer(pattern, line)]
                
                if len(line_num) == 1: #nonempty, number once in line
                    line_nums.append(*line_num)

                # problem: handling 2 times same number in a line
                if len(line_num) > 1:
                    for l in line_num:
                        line_nums.append(l)
        
        # organize by line indices
        where_nums.append(line_nums)
#%%        
engine = array(engine)

# get all characters that appear in engine
not_symbols = list(map(lambda x: str(x), list(range(10)))) + ['.'] 
nums = not_symbols[:-1]
symbols = unique(engine)[isin(unique(engine),
                        not_symbols, invert=True)]

# find all symbol positions
symbols_mask = isin(engine, symbols)
where_rows, where_cols = where(symbols_mask == True)

symbols_pos = {r:where_cols[where(where_rows == r)] for r in where_rows}

part_numbers = []
# loop through all lines where there are symbols
for row in list(symbols_pos.keys()):
    # loop through all symbols
    for symbol in symbols_pos[row]:
        s_idx = (row, symbol)
        
        # Surrounding positions
        above, below = (row - 1, symbol), (row + 1, symbol)
        left, right = (row, symbol - 1), (row, symbol + 1)
        above_left, above_right = (row - 1, symbol - 1), (row - 1, symbol + 1)
        below_left, below_right = (row + 1, symbol - 1), (row + 1, symbol + 1)
        
        surrounds = [above, below, left, right, 
                     above_left, above_right, below_left, below_right]
        
        # Search surrounding positions
        for s in surrounds:
            # the surrounding character is a number
            if engine[s] in nums:
                # look at the coordinates of numbers in row of surrounding character
                line_nums = where_nums[s[0]]
                
                # search through all line_nums (all numbers)
                for j,ln in enumerate(line_nums):
                    # breakpoint()
                    # find coordinates of the number corresponding to the surrounding character
                    if (s[1] >= ln[0] and s[1] <= ln[1]):
                        # drop all nondigit characters from part number
                        part_number = re.sub(r'\D',
                                             '',
                                             str_engine[s[0]][ln[0]:ln[1]])
                        
                        part_numbers.append(int(part_number))
                        
                        # remove those coordinates (prevents double counting same number)
                        # prevents same part-number (adjacent to symbol) from repeating
                        where_nums[s[0]].pop(j)  
                        
print("Part 1:", sum(part_numbers)) #120525 too low, 526144 too low, 860587 too high (duplicates)
# 529447 (before handling twice the same number)

########### I think this is correct... cant figure out why not
# 534297 after handling same number (now two locations if one number multiple times in line)
###########

# WRONG!
# 333894 after only using unique part numbers (not the case ???)
# 531648 considering minus signs !WRONG
