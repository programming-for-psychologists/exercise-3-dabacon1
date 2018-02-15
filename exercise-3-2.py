#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:10:50 2018

@author: DAB
"""

def generateTrials(blocks, masked, sides):
	for block in range(blocks):
		for side in sides:
			for mask in masked:
				trial =",".join([str(block), mask, side])
				print trial

masked = ['masked', 'masked', 'nonmasked']
sides = ['left', 'right']
blocks = 5

generateTrials(blocks, masked, sides) # don't know how to make it start at 0 - what I
                                 # have tried gives me wierd outcomes, but running with 6 blocks, 
                                 # gives me too many trials, so have to run at 5
#python generateTrials.py > trialList.txt