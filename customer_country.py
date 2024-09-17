import csv

def main():
    file_obj = open('customers.csv','r')
    outfile = open('customer_country.csv','w')

    for line in file_obj:
        line = line.split(",")
        outfile.write(f"{line[1]} {line[2]}, {line[4]}" + "\n")

    outfile.close()


main()