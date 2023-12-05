# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:59:47 2023

@author: matus

DAY5
You give a seed a fertilizer
--------
P1 Impossible with the implemented solution because numbers are so big
P2 Seed number ranges
    What is the lowest location number that corresponds to any of the initial seed numbers (within initial seed ranges)?
"""
import re
from numpy import arange

with open('day5_input.txt', 'r') as almanac:
    maps = dict()
    current_map = ""
    for line in almanac:
        # map names
        if ':' in line:
            map_name = re.findall(r"^.*(?=:)", 
                                  line)
            current_map = map_name[0]
            
            maps[current_map] = []
            
            
        # any number separated by word boundary
        nums = re.findall(r"\b(\d+)\b",
                          line)
        # add line numbers to current map list
        if nums != []: # nonempty list
            maps[current_map].append(list(
                        map(lambda x: int(x)
                            ,nums)
                        ))
        pass

# Part 2
maps['seed_ranges'] = []
for i, s in enumerate(maps['seeds'][0]):
    if i % 2 == 0:
        maps['seed_ranges'].append((s,s+maps['seeds'][0][i+1]))

# print(maps['seed_ranges'])
#%%
def make_map_dict (current_dict_vals:list
                   ) -> dict:
    # need to just check whether value larger or smaller than
    # source range = tuple, destination range = tuple
    
    cd = dict()
    for row in current_dict_vals:
        destination_range = (row[0], row[0]+row[-1])
        source_range = (row[1], row[1]+row[-1])

        # for big numbers        
        cd[source_range] = destination_range
        
    return cd
        
        
# Make big dictionary
big_dict = dict()
for map_nam in list(maps)[1:-1]:
    my_map = maps[map_nam]

    big_dict[map_nam] = make_map_dict(my_map)

# print(big_dict)

def find_locations(seeds:list,
                  big_dict:dict,
                  seed_ranges:bool = False) -> list:
    locations = []
    for seed in seeds:
        output = seed # start with seed as the key
        # print(output)
        for now_map in list(big_dict.values()):
            # loop through the tuples, if number >= than source[0] and < source[1]
                # match it to destination by (number - source[0]) + destination[0]
            found = False
            for tuple_range in now_map:
                if output >= tuple_range[0] and output < tuple_range[1]:
                    # print(seed, output, tuple_range, now_map[tuple_range])
                    output = (output - tuple_range[0]) + now_map[tuple_range][0]
                    found = True
                    break
            
            # if source not in map, the destination is the same number
            else:
                if found == False:
                    output = output
                
        # after we have traversed through all the maps
        else:
            locations.append(output)
    
    return locations

locs = find_locations(maps['seeds'][0],
                      big_dict)

print('Part1:', min(locs)) # 57075758
