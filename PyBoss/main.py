# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:32:56 2018

@author: Ind
"""
import os
import csv

CurDataFormat = ["EMP ID","Name","DOB","SSN","State"]
FinalHeaders =["EMP ID","First Name", "Last Name", "DOB", "SSN","State"]
curDataDict={}
FinalDataDict={}
StABB = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
with open("employee_data1.csv")as csvfile:
    csvreader = csv.reader(csvfile)
    
   #csvwriter = csv.writer(new)
    for line in csvreader:
        #print(line[1])
        empID = line[0]
        Namelist = line[1].split()
        DOB = line[2]
        SSN = line[3]
        st = str(line[4])
        abbState = ""
        for key, value in StABB.items():
            if st == key:
                abbState = value
                
        #print (abbState)
        
        # Method1 for reading a list that is a result of the split menthod:
        # In this menthod, since we are extracting the last element in the list
        #for last name and the Last 4 digits of the SNN...we can use -1 as the arg.
        
        FirstName = Namelist[0]
        LastName = Namelist[-1]
        SSNSplit = line[3].split('-')
        FormattedSSN = "***-**-" + SSNSplit[-1]
        
        # Method 2 reading a list that is a result of the split menthod :
        
        DateSplit = line[2].split("-")
        Year = ""
        Date= ""
        Month = ""
        
        for i in DateSplit:
            if DateSplit.index(i)==0:
                #Year
                Year = i
            elif DateSplit.index(i)==1:
                Month  = i
            else:
                Date = i
                
        FormattedDOB = Month +"/"+ Date + "/" +Year
        print(empID+","+FirstName+ "," + LastName+ "," + FormattedDOB+" ," + FormattedSSN+" ," +      abbState)