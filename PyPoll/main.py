# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:32:56 2018

@author: Ind
"""

import os
import csv
#candidates = {"name": "Candidate", "Votes": 0}
#listResults=({}) List of candidates

listResults = []
numVotes = 0

with open("election_data_2.csv","r")as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for line in csvreader:
        candidates={}
        
        numVotes = numVotes+1
        if len(listResults) == 0:
            #This means we are reading the first row with data.
            candidates={"name": line[2],"Votes":1}
            listResults.append(candidates)
        else:
            candiatefound = False
            for CDict in (listResults):
                if CDict["name"] == line[2]: 
                    candiatefound = True
                    #increase the his or her vote count by 1
                    CDict["Votes"] =  CDict["Votes"] + 1
                    break
                
            if(candiatefound==False):
                #Create a new dictonary for this candidate
            
                     candidates={"name": line[2],"Votes":1}
                     listResults.append(candidates)
                     
print (numVotes)                
print(listResults)
           