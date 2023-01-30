import csv

infile = open('customers.csv', 'r', newline = '')
outfile = open('customer_country.csv', 'w', newline = '')

reader = csv.reader(infile, delimiter = ',')

next(reader)
outfile.write('Full Name' + ',' + 'Country' + '\n')



for row in reader:
    outfile.write(row[1] + ' ' + row[2] + ',' + row[4] + '\n')

infile.close()
outfile.close()