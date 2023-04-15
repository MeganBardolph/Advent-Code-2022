#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 13:22:14 2023

@author: laurashelley
"""

## day3_LS

## each rucksack has two large compartments,
#all items of a given type go into one compartment
#elf failed this rule for exactly one item type per rucksack

## instructions: find the errors

## input: list of all items currently in each rucksack
#every item type is identified by a single lowercase or uppercase letter
    #(a and A refer to different item types)
#the list of items for each rucksack is given as characters all on a single line.
#a given rucksack always has the same number of items in each of its two comparmtnents
#so the first half of the characters represent items in the first compartment
#second half is what's in second compartment

## example data (six rucksacks):
# vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw

#the first rucksack contains items vJrwpWtwJgWrhcsFMMfFFhFp
#its first compartment contains     vJrwpWtwJgWr
#its second compartment contains    hcsFMMfFFhFp
#the only item type that appears in both compartments is lowercase p
#1: p
#2: L
#3: P
#4: v
#5: t
#6: s

## to prioritize item rearrangment, each item type can be converted to a priority:
# a-z = priorities 1-26
# A-Z = prioriti3s 27-52

#1: p (16)
#2: L (38)
#3: P (42)
#4: v (22)
#5: t (20)
#6: s (19)
#sum = 157

## find the item type that appears in both compartments of each rucksack.
## what is the sum of the priorities of those item types (one value)

## import some stuff
import string
import numpy as np
from day3_functions_LS import *

## initialize some stuff
item_code = list(string.ascii_lowercase)
item_code.extend(list(string.ascii_uppercase))
priority_code = list(np.arange(1,53))
errs_priority_per_ruck = []

## open and read data line by line
#with open('inputdata_rucksacks_exampledata.txt') as file: #example data
with open('inputdata_rucksacks.txt') as file: #real data
    for line in file:
        errs_priority_per_ruck.append(calc_priority_per_ruck(line,item_code,priority_code)) #calculate priority per line/rucksack

## sum priorities and print
total_priorities_per_ruck = sum(errs_priority_per_ruck)
print('the sum of the priorities of the item types is ', total_priorities_per_ruck)       
        

## part 2 - badges
#elves are divided into groups of three
#each elf in a group carries only one item type in common (their badge)
#need to find the badge for each group,
#need to calculate error priority for each group


## every set of three lines in inputdata corresonds to a single elf group
#group1:
#   vJrwpWtwJgWrhcsFMMfFFhFp
#   jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#   PmmdzqPrVvPwwTWBwg
# r = only item in all 3 rucksacks, their badge type is r
# priority for this group = 18

#group 2:
#    wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#    ttgJtRGJQctTZtZT
#    CrZsJsPPZsGzwwsLwLmpwMDw
# Z = only item typ e in all 3 rucksacks, their badge type is Z  
# priority for this group = 52
      
#sum priorities for the example groups = 70

## initialize some things
errs_priority_per_group = []

## open and read data 3 lines at a time
#with open('inputdata_rucksacks_exampledata.txt') as file:
with open('inputdata_rucksacks.txt') as file:
    for line1, line2, line3 in zip(file, file, file):
        line1 = line1.strip()
        line2 = line2.strip()
        line3 = line3.strip()
        errs_priority_per_group.append(calc_priority_per_group(line1,line2,line3,item_code,priority_code)) #calculate priority per group
               
## sum priorities and print
total_priorities_per_group = sum(errs_priority_per_group)
print('the sum of the priorities per group is ', total_priorities_per_group)       






















