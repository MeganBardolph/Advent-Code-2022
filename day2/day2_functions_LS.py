#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:20:58 2023

@author: laurashelley
"""

## day2 functions file
#call these functions in any day 2 scripts


## calc total rock paper scissors score from strategy guide
def calc_tournament_score(data, strategy):
    score_per_round = []
    
    if strategy == 'myplay':
        for line in data:
            
            #calc shapescore
            if 'X' in line:
                shapescore_tmp = 1
            elif 'Y' in line:
                shapescore_tmp = 2
            elif 'Z' in line:
                shapescore_tmp = 3
            
        
            #calc outcome
            #if opponent throws rock
            if line[0] == 'A': 
                if line[1] == 'X': #draw
                    outcomescore_tmp = 3
                if line[1] == 'Y': #win (paperbeatsrock)
                    outcomescore_tmp = 6
                if line[1] == 'Z': #loss (rockbeatscissors)
                    outcomescore_tmp = 0
        
            #if opponent throws paper
            if line[0] == 'B': 
                if line[1] == 'X': #loss, paperbeatsrock
                    outcomescore_tmp = 0
                if line[1] == 'Y': #draw
                    outcomescore_tmp = 3
                if line[1] == 'Z': #win scissorsbeatspaper
                    outcomescore_tmp = 6
        
            #if opponent throws scissors
            if line[0] == 'C':
                if line[1] == 'X': #win rockbeatsscissors
                    outcomescore_tmp = 6
                if line[1] == 'Y': #loss scissorsbeatspaper
                    outcomescore_tmp = 0
                if line[1] == 'Z': #draw
                    outcomescore_tmp = 3
         
                
            score_per_round.append(shapescore_tmp + outcomescore_tmp)
    
    if strategy == 'outcomeneed':
        for line in data:
            
          
            
            #calc outcome & shapescore
            if line[1] == 'X': #if i must lose
                outcomescore_tmp = 0
                if line[0] == 'A': #if opponent throws rock
                    shapescore_tmp = 3 #i must throw scissors
                if line[0] == 'B': #if opponent throws paper
                    shapescore_tmp = 1 #i must throw rock
                if line[0] == 'C': #if opponent throws scissors
                    shapescore_tmp = 2 #i must throw paper
                
            if line[1] == 'Y': #if i must draw
                outcomescore_tmp = 3
                if line[0] == 'A': #if opponent throws rock
                    shapescore_tmp = 1 #i must throw rock
                if line[0] == 'B': #if opponent throws scissors
                    shapescore_tmp = 2 #i must throw scissors
                if line[0] == 'C': #if opponent throws paper
                    shapescore_tmp = 3 #i must throw paper
                
            if line[1] == 'Z': #if i must win
                outcomescore_tmp = 6
                if line[0] == 'A': #if opponent throws rock
                    shapescore_tmp = 2 #i must throw paper
                if line[0] == 'B': #if opponent throws paper
                    shapescore_tmp = 3 #i must throw scissors
                if line[0] == 'C': #if opponent throws scissors
                    shapescore_tmp = 1 #i must throw rock
            
            score_per_round.append(shapescore_tmp + outcomescore_tmp)

    
    totalscore = sum(score_per_round)
    return totalscore












