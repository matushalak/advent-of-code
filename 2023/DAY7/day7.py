# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:24:15 2023

@author: matus
DAY 7
CAMEL CARDS!
------------------
"""
from numpy import unique, isin

#0) Parse -> hands : bids dictionary
hands = dict()
with open('day7_input.txt', 'r') as camel_cards:
    for line in camel_cards:
        hand, bid = line.split(' ') # returns substrings separated by separator
        hands[hand] = int(bid)
        pass

#1) Get values of and Order hands
cards_map = {'2':1,
            '3':2,
            '4':3,
            '5':4,
            '6':5,
            '7':6,
            '8':7,
            '9':8,
            'T':9,
            'J':10,
            'Q':11,
            'K':12,
            'A':13}

hands_map = {5:1, # High card
             4:2, # One pair
             (3,2):3, # Two pair
             (3,3):4, # Three of a kind
             (2,3):5, # Full house
             (2,4):6, # Four of a kind
             1:7} # Five of a kind

def get_hands_map (hands, hands_map, joker = False)-> dict:
    hands_by_value = {k:[] for k in list(hands_map.values())}
    for hand in list(hands):
        hand_l  = list(hand)
        unq = unique(hand_l)
        nunq = unq.shape[0]
        
        # Part 2
        jokers = None
        if joker == True:
            jokers = sum(isin(hand_l, 'J'))

        # -> upgrade if Joker part of the 'other' cards
        # Five of a kind -> Five of a kind
        if nunq == 1:
            hand_val = 1
        
        elif nunq == 2:
            # Four of a kind -> Five of a kind
            if sum(isin(hand_l, unq[0])) == 1 or sum(isin(hand_l, unq[0])) == 4:
                if jokers in (1,4):
                    hand_val = 1 # upgrades 4 of a kind to 5 of a kind
                else:
                    hand_val = (2,4) # Four of a kind
            
            # Full house -> Five of a kind (if 2 or 3 jokers)
            else:
                if jokers in (2,3):
                    hand_val = 1 # upgrades to 5 of a kind
                else:
                    hand_val = (2,3) # Full house
        
        elif nunq == 3:
            sums = [sum(isin(hand_l, i)) for i in unq]
            # Three of a kind -> Four of a kind 
            if 3 in sums:
                if jokers in (3,1):
                    hand_val = (2,4) # upgrade to 4 of a kind
                else:
                    hand_val = (3,3) # Three of a kind 
                    
            # Two pair -> Full house (if 1 joker)
            else:
                if jokers == 2:
                    hand_val = (2,4) # upgrade to four of a kind
                elif jokers:
                    hand_val = (2,3) # upgrade to full house
                else:
                    hand_val = (3,2) # Two pair
        
        # One pair -> Three of a kind (if 1 joker)
        elif nunq == 4:
            if jokers:
                hand_val = (3,3) # upgrade to three of a kind
            else:
                hand_val = 4 # One pair
        
        # High card -> One pair (if 1 joker)
        else:
            if jokers:
                hand_val = 4 # upgrade to one pair
            else:
                hand_val = 5 # High card
        
        hands_by_value[hands_map[hand_val]].append(hand)    

    return hands_by_value
        
hands_by_type = get_hands_map(hands, hands_map)

#%%2) Order within hands
# use comparator to sort
from functools import cmp_to_key

def compare_within_type(x,y):
    x,y = list(x), list(y)
    
    for card1, card2 in zip(x,y):
        if cards_map[card1] > cards_map[card2]:
            return 1
        elif cards_map[card1] < cards_map[card2]:
            return -1

def get_winnings(cards_map,
                 hands_by_type,
                 hands,
                 comparator):
    sorted_hand_types = []
    for hand_type in list(hands_by_type):
        sorted_hand_types += sorted(hands_by_type[hand_type], 
                                    key = cmp_to_key(comparator),
                                    reverse=False)
                         
    winnings = []
    rank_bid = dict()
    for i,h in enumerate(sorted_hand_types):
        rank_bid[i+1] = hands[h]
        winnings.append((i+1)*hands[h])

    return winnings

print("Part1:", sum(get_winnings(cards_map,
                                 hands_by_type,
                                 hands,
                                 compare_within_type))) #251058093

#%% Part 2 - Jokers, just change how types are calculated, some more if statements
card_map2 = {'2':1,
            '3':2,
            '4':3,
            '5':4,
            '6':5,
            '7':6,
            '8':7,
            '9':8,
            'T':9,
            'J':0, # lowest individual value
            'Q':11,
            'K':12,
            'A':13}

# couldn't specify parameters for comparator function so had to make a new one...
def compare2(x,y):
    x,y = list(x), list(y)
    
    for card1, card2 in zip(x,y):
        if card_map2[card1] > card_map2[card2]:
            return 1
        elif card_map2[card1] < card_map2[card2]:
            return -1

hands_by_type2 = get_hands_map(hands, hands_map, joker = True) #P2

print("Part2:", sum(get_winnings(card_map2,
                                 hands_by_type2,
                                 hands,
                                 compare2))) # P2: 249781879