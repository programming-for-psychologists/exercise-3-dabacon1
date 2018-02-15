#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:44:05 2018

@author: DAB
"""
import random 

def generateTrials(blocks, masked, sides):
    trialList=[]
    for block in range(blocks):
		for side in sides:
			for mask in masked:
				trial =",".join([str(block), mask, side])
				trialList.append(trial)

    random.shuffle(trialList)
    for trial in trialList:
            print trial
            
masked = ['masked', 'masked', 'nonmasked']
sides = ['left', 'right']
blocks = 5
trialList = generateTrials(blocks,masked,sides) # see 3-2
#python generateTrials.py > trialList.txt