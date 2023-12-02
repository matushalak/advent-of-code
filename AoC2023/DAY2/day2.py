# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:52:37 2023
@author: matus

Day2 AoC 2023
Cube Conundrum
---------------
game:
    small bag with red / green / blue cubes
    Goal: How many cubes, what kind in the bag
    multiple times a game (Game X), 
    draw random cubes 
    & see how many of each color (with replacement)
    (each draw separated by ;)
    
    play multiple games

part 1:
    which games would have been POSSIBLE with
    12 red, 13 green, 14 blue cubes
"""
import re
from numpy import cumprod

def is_game_possible(known_contents:list[int,int,int], 
                     game:str,
                     ) -> (bool, int):
    
    game_contents = {'red':[],
                     'green':[],
                     'blue':[]}
    
    possible_colors = []
    mins = [] #part 2
    
    for i, color in enumerate(list(game_contents.keys())):
        # if color was drawn
        if color in game:
            # find all occurrences of that color
            where_colors = [m.span(0)[0] for m in re.finditer(color, game)]
            
            # check from -3, to color start (that;s where the numbers will be)
            for w in where_colors:
                value = int(game[w-3:w])
                game_contents[color].append(value)
            
        if max(game_contents[color]) <= known_contents[i]:
            possible_colors.append(True)
        else:
            possible_colors.append(False)
        
        # part 2: min number necessary = max number found
        mins.append(max(game_contents[color]))
    
    # print(game_contents)
    # print(mins, cumprod(mins)[-1])
    # print(game)
    
    return (all(possible_colors), cumprod(mins)[-1])

possible_games = [] # part 1
powers = [] # part2
with open('day2_input.txt', 'r') as all_games:
    for gn, game in enumerate(all_games): # line
        possible, power = is_game_possible([12,13,14],
                                            game)
        # Part 2
        powers.append(power)
        
        # Part 1
        if possible == True:
            possible_games.append(gn+1)
            
            
print('Part 1 result:', sum(possible_games))
print('Part 2 result:', sum(powers))

