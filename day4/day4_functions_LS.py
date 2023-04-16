#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:29:07 2023

@author: laurashelley
"""

## day4_fucntions_LS

def find_overlap(line): #returns 1 if full overlap, 0 if not full overlap
    import numpy as np
    import re
    
    ## use regex here to extract the numbers, whether they are one or more digits
    pattern = r'\d+-\d+' #match one or more digits followed by a hyphen and one or more digits
    matches = re.findall(pattern,line)
    
    ## extract the numbers as integers
    pair = [int(num) for match in matches for num in match.split('-')] #for each match/string in list, and for each number on left vs right of hyphen, get integer
    
    ## create sets that contain all numbers in range and compare
    elf1_secs = list(np.arange(pair[0], pair[1]+1)) #all sections for elf1
    elf2_secs = list(np.arange(pair[2], pair[3]+1)) #all sections for elf2
    if set(elf1_secs).issubset(elf2_secs) or set(elf2_secs).issubset(elf1_secs): #if one fully contains the other
        full_overlap = 1 #yes one fullly contains the other
    else:
        full_overlap = 0 #no full overlap
        
    if set(elf1_secs).intersection(elf2_secs):
        any_overlap = 1
    else:
        any_overlap = 0
    return full_overlap, any_overlap







