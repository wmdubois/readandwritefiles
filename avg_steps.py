print()

import csv

def main():
    infile = open("steps.csv","r")
    infile.readline()
    month = ['January','February','March','April','May','June','July','August','September','October','November','December']


    for line in infile:
        line = line.rstrip("\n").split(",")
        #print(line)
        while line[1] == '1':
            










main()