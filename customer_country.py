import csv
infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)

outfile = open('customer_country.csv','w')
writer = outfile

writer.write("Full Name, Country\n")

for record in csvfile:
    FN = record[1]
    LN = record[2]
    CNTRY = record[4]
    writer.write(FN +' ')
    writer.write(LN + ', ')
    writer.write(CNTRY + "\n")

outfile.close()
        



