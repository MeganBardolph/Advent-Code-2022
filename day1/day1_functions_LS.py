#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:34:36 2023

@author: laurashelley
"""

## Day1 functions
#call these functions in the day1 script


## calculate, line by line, total calories for each elf and append to total_cals_per_elf
def tot_cals_per_elf(data): 
    total_cals_per_elf = []
    for item in data:
        tmp = item.split('\n')
        tmptmp = []
        for i in tmp:
            tmptmp.append(int(i))
        total_cals_per_elf.append(sum(tmptmp))

    return total_cals_per_elf


## calculate total calories for each elf and return a list of the top NUM (top 3? top 4? etc)
def top_NUM_elf_cals(data,num_elves):
    total_cals_per_elf = tot_cals_per_elf(data)
    total_cals_per_elf.sort(reverse=True)
    return total_cals_per_elf[0:num_elves]






