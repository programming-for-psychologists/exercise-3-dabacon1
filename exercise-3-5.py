#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:44:19 2018

@author: DAB
"""

import random 

def generateTrials(blocks, masked, sides):
    
    for block in range(blocks):
        trialList=[] 
        x = 0
        while x <2:
            for side in sides:
                for mask in masked:
    				trial =",".join([str(block), mask, side])
    				trialList.append(trial)
    x = x +1
    random.shuffle(trialList)
    for trial in trialList:
            print trial
    return trialList
            
masked = ['masked', 'masked', 'nonmasked']
sides = ['left', 'right']
blocks = 5
trialList = generateTrials(blocks,masked,sides)
#python generateTrials.py > trialList.txt