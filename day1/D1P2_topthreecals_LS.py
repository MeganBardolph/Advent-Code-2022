#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:24:14 2023

@author: laurashelley
"""

## day 1, part 2
## find the top three elves carrying the most calories, how many calories total?

## load input data from a txt file and split per elf (blank line btwn elves)
#rawdata = open('inputdata_cals_exampledata.txt').read() #example data - for accuracy check
rawdata = open('inputdata_cals.txt').read() #input actual data
data = rawdata.split('\n\n')


#get list of top 3 elf calorie counts
from day1_functions import top_NUM_elf_cals
top3_cals = top_NUM_elf_cals(data,3)

#calc sum of top 3
top3_total_cals = sum(top3_cals)
print('the total calories for the top 3 elves is ', top3_total_cals, 'calories')









