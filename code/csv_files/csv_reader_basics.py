#This is a file to read a csv file and input the data back into the module

import csv
#data input

time = []
bpm = []
volts = []
#sets variable names
with open('exampledata.csv') as csvdata:
    csvreader = csv.reader(csvdata)
    for row in csvreader:
#opens file and reads the csv data splitting it up into rows which then are set
#below as being data according to the variables        
        time.append(row[0])
        bpm.append(row[1])
        volts.append(row[2])

print(time)
print(bpm)
print(volts)
#prints data

#this would be used in conjunction with the write to read the data with this
#first then edit in events from bluetooth before being written back 
