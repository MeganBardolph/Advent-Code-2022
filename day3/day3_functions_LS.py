#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 16:00:27 2023

@author: laurashelley
"""

#day3_functions_LS

## calculates error priority for items per rucksack
def calc_priority_per_ruck(line,item_code,priority_code):
    c1tmp = line[0:int(len(line)/2)] #grab items in first compartment
    c2tmp = line[int(len(line)/2):] #grab items in second compartment
    errstmp = set(c1tmp).intersection(c2tmp) #compare compartments to find common item
    errstmp = list(errstmp) #change from set to list
    errs_priority_tmp = priority_code[item_code.index(errstmp[0])] #find priority code from item code
    
    return errs_priority_tmp


## calculates error priority for badges in group
def calc_priority_per_group(line1,line2,line3,item_code,priority_code):
    errstmp = set(line1).intersection(line2,line3) #compare rucksacks to find common item
    errstmp = list(errstmp) #change from set to list
    errs_priority_tmp = priority_code[item_code.index(errstmp[0])] #find priority code from item code
    
    return errs_priority_tmp
