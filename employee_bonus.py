import csv

infile = open('EmployeePay.csv', 'r', newline = '')

reader = csv.reader(infile, delimiter = ',')

field_names = next(reader)

print(format(field_names[0], '8'), format('Full Name', '24'), format(field_names[3], '9'),field_names[4])

for row in reader:
    print(format(row[0], '8'), format(row[1] +' ' + row[2], '25'), format(row[3], '10'), format(row[4], ''), sep = '')

infile.close()
