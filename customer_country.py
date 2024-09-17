import csv

def main():
    file_obj = open('customer.csv','r')
    outfile = open('customer_country.csv','w')

    for rec in file_obj: