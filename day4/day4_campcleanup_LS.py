#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:28:18 2023

@author: laurashelley
"""

## day4_campcleanup_LS


## elves have been assigned to clean up seections of the cam
#every section has a unique ID number and each elf is assigned a range of section IDs
#some of the elves compare their section assignments, and many of the assignents overlap
#to try to quickly find overlaps, the elves pair up and make a big list of section assignments for each pair (puzzle input)

## example section assignment list for elf pairs
# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7 ##full overlap
# 6-6,4-6 ##full overlap
# 2-6,4-8

#within the first pair, the first elf was assigned sections 2,3,4
#while the second pair was assigned sections 6,7,8

#some of the pairs have noticed that one of their assignments fully contains the other
#2-8 fully contains 3-7
#6-6 is fully contained in 4-6
#there are 2 such pairs in the exampledata

## in how many assignment pairs does one range fully contain the other?

## import some stuff
from day4_functions_LS import find_overlap

## initialize some stuff
full_overlap_list = []

## find full overlap
#with open('inputdata_campcleanup_exampledata.txt') as file:
with open('inputdata_campcleanup.txt') as file:
    for line in file:
        full_overlap_list.append(find_overlap(line)[0])

## count total pairs with full overlap and print
num_full_overlap = sum(full_overlap_list)
print(num_full_overlap, ' assignment pairs have one range fully containing another')


##############################################################################3
## part 2
#still a lot of duplicate work planned
#now the elves want to know the number of pairs that have any ovelrap AT ALL (including partial overlap)

## initialize some stuff
any_overlap_list = []

## find any overlap
#with open('inputdata_campcleanup_exampledata.txt') as file:
with open('inputdata_campcleanup.txt') as file:
    for line in file:
        any_overlap_list.append(find_overlap(line)[1])

## count total pairs with any overlap and print
num_any_overlap = sum(any_overlap_list)
print(num_any_overlap, ' assignment pairs have any overlap at all')











