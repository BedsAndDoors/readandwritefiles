import csv
from tkinter import Y

infile = open('customers.csv','r')
csvfile = csv.reader(infile,delimiter=',')
for record in csvfile:
    print('ID:    ', record[0])
    print('FN:    ', record[1])
    print('LN:    ', record[2])
    print('City:  ', record[3])
    print('CNTRY: ', record[4])
    print('Phone: ', record[5])

    input()
    