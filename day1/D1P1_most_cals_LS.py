#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:28:55 2023

@author: laurashelley
"""

## Day 1, part 1
## first challenge is to find the elf carrying the most calories, and how many
## calories is that?


## load input data from a txt file and split per elf (blank line btwn elves)
#rawdata = open('inputdata_cals_exampledata.txt').read() #example data - for accuracy check
rawdata = open('inputdata_cals.txt').read() #input actual data
data = rawdata.split('\n\n')


## calc total calories per elf
## call tot_cals_per_elf from day1_functions file
from day1_functions_LS import tot_cals_per_elf
total_cals_per_elf = tot_cals_per_elf(data)




##find max calories and print
max_cals_elf = max(total_cals_per_elf)
print('The elf with the most calories has ', max_cals_elf, 'calories')




