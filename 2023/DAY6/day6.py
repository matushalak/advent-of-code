# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:59:39 2023

@author: matus

DAY 6
Part 1:
    go farther in each race than the current record holder
    
Part 2:
    just one big race
"""
import re
from numpy import cumprod

def get_times_records (input_file,
                       one_race = False):
    with open(input_file, 'r') as races:
        for line in races:
            
            if one_race == False:
                nums = list(map(lambda x: int(x), re.findall(r"\b(\d+)\b", 
                                                             line)
                                ))
            
            else:
                nums = int(''.join(re.findall(r"\b(\d+)\b", 
                                              line))
                           )
            
            if "Time" in line:
                max_race_times = nums
            
            else:
                record_distances = nums
            
    
    print("Allowed_time(s):", max_race_times)
    print("Current record(s):", record_distances)
    
    return max_race_times, record_distances

def find_ways_to_beat (input_f,
                       bad_kerning = False,
                       optimize = False):
    ways_to_beat = []
    speeds_that_beat = []
    
    if bad_kerning == False:
        for time, record in zip(*get_times_records(input_f,
                                                   bad_kerning)):
            ways_to_beat_record = 0
            speeds_to_beat_record = []
            # min boat speed is 1 ms, max is time -1 (otherwise boat doesn't move)
            for speed in range(1, time):
                if speed * (time - speed) > record:
                    ways_to_beat_record += 1
                    speeds_to_beat_record.append(speed)
            
            ways_to_beat.append(ways_to_beat_record)
            speeds_that_beat.append(speeds_to_beat_record)
    else:
        time, record = get_times_records(input_f, bad_kerning)
        
        ways_to_beat_record = 0
        # speeds_to_beat_record = []
        # min boat speed is 1 ms, max is time -1 (otherwise boat doesn't move)
        for speed in range(1, time):
            if speed * (time - speed) > record:
                ways_to_beat_record += 1
                # speeds_to_beat_record.append(speed)
        
        ways_to_beat.append(ways_to_beat_record)
        # speeds_that_beat.append(speeds_to_beat_record)
        
    # print(ways_to_beat)
    # print(speeds_that_beat)
    
    if bad_kerning == False:
        print('Part 1:', cumprod(ways_to_beat)[-1])
        
    else:
        print('Part 2:', *ways_to_beat)
        
find_ways_to_beat('day6_input.txt', bad_kerning=False) # 500346
find_ways_to_beat('day6_input.txt', bad_kerning=True) #42515755