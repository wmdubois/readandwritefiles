import csv

def main():
    infile = open('customers.csv','r')
    outfile = open('customer_country.csv','w')

    for line in infile:
        line = line.split(",")
        outfile.write(f"{line[1]} {line[2]}, {line[4]}" + "\n")

    outfile.close()


main()