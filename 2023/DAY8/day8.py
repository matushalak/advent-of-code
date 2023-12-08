# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:55:48 2023

@author: matus
DAY8
----------
Haunted Wasteland

How many steps to find ZZZ
"""
import re
from numpy import lcm, array, zeros

maps = {}
with open('day8_input.txt', 'r') as d8:
    for i, line in enumerate(d8):
        if i == 0:
            # left = 0, right = 1
            directions = list(map(lambda x: 0 if x == 'L' else 1,line[:-1]))
            
        elif '=' in line:
            map_from = re.findall(r"^.*(?= =)", 
                                  line)[0]
            
            # maps_to [0] = left, maps_from [1] = right
            maps_to = re.findall(r'\(([^)]+), ([^)]+)\)',
                                 line)[0]
            
            maps[map_from] = maps_to

# print(maps)

# P1
def solve (maps, directions, start_node = 'AAA', p1 = True):
    steps = 0
    
    node = start_node
    # print(node)
    if p1 == True:        
        while node != 'ZZZ':
            for d in directions:
                node = maps[node][d]
                steps += 1
                
        else:
            # print(node, steps)
            return steps
    
    else: # P2
        while node[-1] != 'Z':
            for d in directions:
                node = maps[node][d]
                steps += 1

        else:
            # print(node, steps)
            return steps
    
    # Part 2
    # start nodes
nodes = [nd for nd in list(maps) if nd[-1] == 'A']
z_nodes = [solve(maps, directions, start_node=node, p1 = False)
           for node in nodes]
#%% Solutions
print('Part 1:', solve(maps, directions, p1 = True)) # P1 : 12169
# to get Lowest Common Multiple from a whole array,
# need to "reduce" 
print('Part 2:', lcm.reduce(z_nodes,dtype = 'int64')) # P2 : 12030780859469