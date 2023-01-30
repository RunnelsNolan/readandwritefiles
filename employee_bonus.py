import csv

infile = open('EmployeePay.csv', 'r', newline = '')

reader = csv.reader(infile, delimiter = ',')

next(reader)

for row in reader:
    print(format(row[0], '8'), format(row[1] +' ' + row[2], '25'), format(row[3], '10'), format(row[4], ''))

infile.close()
