print()

import csv

def main():
    infile = open("steps.csv","r")
    infile.readline()
    month_name = ['January','February','March','April','May','June','July','August','September','October','November','December']
    month_steps = [0,0,0,0,0,0,0,0,0,0,0,0]
    month_days = [0,0,0,0,0,0,0,0,0,0,0,0]
    avg_steps = [0,0,0,0,0,0,0,0,0,0,0,0]

    x=0
    for line in infile:
        line = line.rstrip("\n").split(",")
    
        if x + 1 == int(line[0]):
            month_steps[x] += int(line[1])
            month_days[x] += 1
        else:
            x+=1
            month_steps[x] += int(line[1])
            month_days[x] += 1

    for s in range(12):
        avg_steps[s] += (month_steps[s] / month_days[s])
        print(f"{month_name[s]} - {'{:,.2f}'.format(avg_steps[s])}")
                   

main()