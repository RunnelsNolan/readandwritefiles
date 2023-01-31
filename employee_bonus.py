import csv

infile = open('EmployeePay.csv', 'r', newline = '')

reader = csv.reader(infile, delimiter = ',')

field_names = next(reader)

print(format(field_names[0], '8'), format('Full Name', '24'), format(field_names[3], '9'),format(field_names[4],'10'), 'Total Pay')

for row in reader:
    salary = int(row[3])
    bonus_rate = float(row[4])
    bonus = salary * bonus_rate
    total_pay = bonus + salary
    print(format(row[0], '8'), format(row[1] +' ' + row[2], '25'), format(row[3], '7'), format(bonus,'10.2f'), format(total_pay,'12.2f'), sep = '')
    input() #pause processing

infile.close()
