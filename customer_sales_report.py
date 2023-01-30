import csv

infile = open('sales.csv', 'r', newline = '')
outfile = open('salesreport.csv', 'w', newline = '')
reader = csv.reader(infile, delimiter = ',')

next(reader)


outfile.write('Customer ID' + ',' + 'Total' + '\n')

cust_total = 0
cust_id = ''

for row in reader:
    sub_total = float(row[3])
    tax_amount = float(row[4])
    freight = float(row[5])
    
    if cust_id == '':
        cust_id = str(row[0])
    
    if cust_id == row[0]:
        line_total = sub_total + tax_amount + freight
        cust_total += line_total
       
    
    else:
       #convert cust_total to 2 decimal points and then a string to i can concatenate
        cust_total = format(cust_total, '.2f')
        cust_total = str(cust_total)
        
        outfile.write(cust_id + ',' + cust_total + '\n')
        
        cust_total = 0
        
        cust_id = str(row[0])
        line_total = sub_total + tax_amount + freight
        cust_total += line_total
  

#have to print out the last value outside of the loop
cust_total = format(cust_total, '.2f')
cust_total = str(cust_total)

outfile.write(cust_id + ',' + cust_total + '\n')
   
infile.close()
outfile.close() 

