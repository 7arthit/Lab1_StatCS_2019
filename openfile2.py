import csv
with open('test2.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f) 
    for row in reader: 
        for field in row:
            print(field)
with open('test2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
        print(row)

import numpy as np 
with open("test2.txt") as in_fi:
    lines = in_fi.readlines()
    no = []
    name = []
    price = []
    print(lines)
    for line in lines:
        txt = line.split(',')
        no.append(int(txt[0]))
        print(no)
        name.append(txt[1])
        print(name)
        price.append(float(txt[2]))
        print(price)
price=np.array(price)
print(np.amin(price))
print(np.amax(price))
print(np.mean(price)) 
print(np.var(price)) 
print(np.std(price)) 
print(np.median(price))

print('===========================')
print('no\tname\tprice')
print('===========================')
for i in range(0,len(no)):
    print('%d\t%s\t%.2f'%(no[i],name[i],price[i]))
print('===========================')

with open('test2.csv') as csv_fi:
    lines = csv.reader(csv_fi)
    no = []
    name = []
    price = []
    print(lines)
    for line in lines:
        print(line)
        for (i,txt) in enumerate(line):
            if i==0: no.append(int(txt))
            if i==1: name.append(txt)
            if i==2: price.append(float(txt))

with open('test_out.txt','w') as out_fi:
    out_fi.write('===========================\n')
    out_fi.write('no\tname\tprice\n')
    out_fi.write('===========================\n')
    for i in range(0,len(no)):
        out_fi.write('%d\t%s\t%.2f\n'%(no[i],name[i],price[i]))
        out_fi.write('===========================\n')
