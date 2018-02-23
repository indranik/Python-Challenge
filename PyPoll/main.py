# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:32:56 2018

@author: Ind
"""

import os
import csv
#candidates = {"name": "Candidate", "Votes": 0}
#listResults=({}) List of candidates

listResults = ()
numVotes = 0

with open("election_data2.csv","r")as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for line in csvreader:
        if len(listResults) == 0:
            #This means we are reading the first row with data.
            candidates={"name": line[2],"Votes":1}
            listResults = (candidates)
        else:
            candiatefound = false
            for dicts in listResults:
                if
            
            
