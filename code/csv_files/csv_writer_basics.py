#This is a file to write a set of numbers into a csv file
import csv
#data imput
csvdata =[['Time', 'BPM', 'Volts'], ['5', '94', '0.3'], ['6', '103', '0.5'], ['7','84','0.2']]
#name of file to write to and inputting the data as rows in an array
with open('exampledata.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvdata)

csvFile.close()
#basic  setup where the only thing which needs changing is the csv data needs to be
#connecting to the inputs of the sensors at time (t) which is written in the first column
