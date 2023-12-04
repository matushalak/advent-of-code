# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:57:01 2023

@author: matus

DAY4: 
SCRATCHCARDS
--------------
Part 1: How many points?
Part 2: How many scratchcards?
-> once you process the current card, no other card can increase its number
"""
import re
from numpy import isin, ones

# Part 1 - Very intuitive and nice
with open('day4_input.txt', 'r') as scratchcards:
    winning, my, points, additional_cards = [],[], [], []
    for scratchcard in scratchcards:
        start, half = scratchcard.find(":"), scratchcard.find("|")
        winning_str, my_str = scratchcard[start:half], scratchcard[half:]
        
        pattern = r"\b([0-99]{1,2})\b"
        wn, mn = re.findall(pattern, winning_str), re.findall(pattern, my_str)
        
        winning.append(list(map(lambda x: int(x), wn))), my.append(list(map(lambda x: int(x), mn)))
        
        # How many matches in given card => How many of subsequent cards you win
        how_many = sum(isin(wn, mn))
        
        # P2
        additional_cards.append(how_many)
        
        if how_many > 0:
            points.append(2 ** (how_many - 1))
            # print(how_many, 2 ** (how_many - 1))
        else:
            points.append(0)
    print('Part1:', sum(points))
    
# Part 2: Quite hard
how_many_cards = ones(len(additional_cards)) # by default one of each card

# additional_cards tells you which other cards a given card affects
for i, additional in enumerate(additional_cards):
    # start with adding ones, later depends on how many copies had been added before
    how_much_add = how_many_cards[i]    
    # add instance of card to n next cards based on n matches
    how_many_cards[i+1:i+additional+1] += how_much_add
        
print('Part2:', sum(how_many_cards.astype(int)))

# 8278 too low
# 15950 too low
# 6857330 the right answer