import csv
infile = open('EmployeePay.csv', 'r')
csvfile = csv.reader(infile,delimiter=',')

for row in csvfile:
    x=1
    FN = row[x,1] + row[x,2]
    PAY = float(row[x,3])
    BNS = float(row[x,4])
    TBNS = PAY*BNS
    TOT = PAY+TBNS
    print(FN, TOT)
    x+=1
    input('Continue?: ')


