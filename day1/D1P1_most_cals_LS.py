#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 15:28:55 2023

@author: laurashelley
"""

## first challenge is to find the elf carrying the most calories, and how many
## calories is that?


## load input data from a txt file
#rawdata = open('inputdata_cals_exampledata.txt').read() #example data - for accuracy check
rawdata = open('inputdata_cals.txt').read() #input actual data
data = rawdata.split('\n\n')
total_cals_per_elf = []

for item in data:
    tmp = item.split('\n')
    tmptmp = []
    for i in tmp:
        tmptmp.append(int(i))
    total_cals_per_elf.append(sum(tmptmp))

max_cals_elf = max(total_cals_per_elf)





