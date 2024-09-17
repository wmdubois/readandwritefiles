print()


import csv

def main():
    infile = open("employee_data.csv","r")
    category = infile.readline().rstrip("\n").split(",")

    for line in infile:
        line = line.rstrip("\n").split(",")
        bonus_value = (float(line[7]) * float(line[3]))
        pay_value = (float(line[3]) + bonus_value)


        print(f"{category[1]}: {line[1]}")
        print(f"{category[3]}: {'${:,.2f}'.format(float(line[3]))}")
        print(f"{category[7]}: {'${:,.2f}'.format(bonus_value)}")
        print(f"Pay: {'${:,.2f}'.format(pay_value)}")
        print()

    





main()