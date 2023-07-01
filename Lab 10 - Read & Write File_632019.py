#อาทิตย์ ทวีบท 63011212019
import csv
import numpy
def schooldata():
    with open('schooldata.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for field in row:
                print(field, end=' \t')
            print()

def pizzadata():
    data = []
    with open("Lab10.txt", 'w') as out_fi:
        with open("pizzadata.txt", encoding='utf-8') as f:
            for lines in f:
                txt = lines.split('	')
                data.append(float(txt[4]))
                for i in range(1, 5):
                    if(i==4):
                        out_fi.write(txt[i])
                    else:
                        out_fi.write(txt[i]+' \t')
            out_fi.write('\n')
            out_fi.write('Min= \t\t\t%.2f \n'%min(data))
            out_fi.write('Max= \t\t\t%.2f \n'%max(data))
            out_fi.write('Mean= \t\t\t%.2f \n'%numpy.mean(data))
            out_fi.write('Variance= \t\t%.2f \n'%numpy.var(data))
            out_fi.write('Sd= \t\t\t%.2f \n'%numpy.std(data))
            out_fi.write('Median= \t\t%.2f \n'%numpy.median(data))
while True:
    print('Main Menu')
    print('1.schooldata.csv')
    print('2.pizzadata.txt')
    print('3.Quit\n')
    choice=''
    try:
        choice=int(input('Enter choice:'))
    except ValueError:
        print('invalid choice. Enter 1-3\n')
        continue
    if choice==1:
        schooldata()
        continue
    if choice==2:
        pizzadata()
        continue
    if choice==3:
        print('Quit\n')
        break
