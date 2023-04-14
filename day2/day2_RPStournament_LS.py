#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:12:41 2023

@author: laurashelley
"""

## rock paper scissors tournament


## PART 1 #####################################################################
## calculate total score if everything goes exactly according to strategy guide

## encrypted strategy guide
# col 1: what your opponent is going to play: A=rock, B=paper, C=scissors
# col 2: UNKNOWN, but, what you should play in response?: X=rock, Y=paper, Z=scissors


## scoring
# score for shape you selected: 1 for rock(X), 2 for paper(Y), 3 for scissors(Z)
# plus
# score for the outcome of the round: 0 if you lost, 3 if the round was a draw, and 6 if you won 

## note: total score is calculated weird because the number assigned to the shape selected is confounded with the outcome score??

## Sample strategy guide
# A Y = 8 points (2 + 6)
# B X = 1 points (1 + 0)
# C Z = 6 points (3 + 3)
#
# total score = 15


#read in the data rom a txt file, split per line (\n)
#rawdata = open('inputdata_strategyguide_exampledata.txt').read() #input example data for accuracy check
rawdata = open('inputdata_strategyguide.txt').read()
datatmp = rawdata.split('\n')
data = [x.split(' ') for x in datatmp] #split on space - makes list of lists

## calculate total score from strategy guide
# call calc_tournament_score from functions file
from day2_functions_LS import calc_tournament_score
totalscore = calc_tournament_score(data,'myplay') #pass it data, and col 2 definition (myplay vs outcomeneed)

## output total score
print('according to part 1 where column 2 dictates what you should throw to win, your total score is ', totalscore)      
    
    





## PART 2 #####################################################################
## elf says column 2 is how the round needs to end: X=you need to lose, Y=you need to draw, Z=you need to win
## scoring still the same

## encrypted strategy guide
# col 1: what your opponent is going to play: A=rock, B=paper, C=scissors
# col 2: how the round needs to end: X=you need to lose, Y=you need to draw, Z=you need to win

## scoring
# score for shape you selected: 1 for rock(X), 2 for paper(Y), 3 for scissors(Z)
# plus
# score for the outcome of the round: 0 if you lost, 3 if the round was a draw, and 6 if you won 

## Sample strategy guide
# A Y = 8 points (1 + 3)
# B X = 1 points (1 + 0)
# C Z = 6 points (1 + 6)
#
# total score = 12

#calculate total score from strategy guide
totalscore = calc_tournament_score(data, 'outcomeneed') #pass it data, and col 2 definition (myplay vs outcomeneed)
print('according to part 2 where column 2 dictates needed outcome, your total score is ', totalscore)   

























