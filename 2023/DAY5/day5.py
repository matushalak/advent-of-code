# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:59:47 2023

@author: matus

DAY5
You give a seed a fertilizer
--------
P1 Impossible with the implemented solution because numbers are so big
"""
import re
from numpy import arange

with open('day5_example.txt', 'r') as almanac:
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

def make_map_dict (current_dict_vals
                   ) -> dict:
    # need to just check whether value larger or smaller than
    # source range = tuple, destination range = tuple
    # loop through the tuples, if number >= than source[0] and < source[1]
        # match it to destination by (number - source[0]) + destination[0]
    cd = dict()
    for row in current_dict_vals:
        destination_range = arange(row[0], row[0]+row[-1])
        source_range = arange(row[1], row[1]+row[-1])
        
        if cd == {}:
            cd = {s:d for s,d in zip(source_range,destination_range)}
        
        else:
            for s,d in zip(source_range,destination_range):
                cd[s] = d
    return cd
        
        
# Make big dictionary
big_dict = dict()
for map_nam in list(maps)[1:]:
    my_map = maps[map_nam]

    big_dict[map_nam] = make_map_dict(my_map)

# print(big_dict)

def find_locations(seeds,
                  big_dict) -> list:
    locations = []
    for seed in seeds:
        output = seed # start with seed as the key
        
        for now_map in list(big_dict.values()):
            try:
                output = now_map[output]
            # if source not in map, the destination is the same number
            except KeyError:
                output = output
        # after we have traversed through all the maps
        else:
            locations.append(output)
    
    return locations

locs = find_locations(maps['seeds'][0],
                      big_dict)

print('Part1:', min(locs))
