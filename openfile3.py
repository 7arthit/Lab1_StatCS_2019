import csv
with open('test2.csv') as csv_fi:
    lines = in_fi.readlines()
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
