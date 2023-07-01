#อาทิตย์ ทวีบท 63011212019
import csv
import numpy
def schooldata():
    with open('schooldata.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for field in row:
                print(field, end=' \t')
            print()
def pizzadata():
    with open("pizzadata.txt", encoding='utf-8') as file:
            for lines in file:
                txt = lines.split('	')
                x.append(float(txt[4]))         
            for i in range(1, 5):
                if(i==4):
                    out_fi.write(txt[i])
                else:
                    out_fi.write(txt[i]+' \t')
    x = []
    with open("test_Lab11.txt", 'w') as out_fi:
            out_fi.write('\n======================================\n')
            out_fi.write('Min= \t\t\t%.2f \n'%min(x))
            out_fi.write('Max= \t\t\t%.2f \n'%max(x))
            out_fi.write('Mean= \t\t\t%.2f \n'%numpy.mean(x))
            out_fi.write('Variance= \t\t%.2f \n'%numpy.var(x))
            out_fi.write('Sd= \t\t\t%.2f \n'%numpy.std(x))
            out_fi.write('Median= \t\t%.2f \n'%numpy.median(x))
# main
print("Menu")
print("[1] Menu อ่าน schooldata.csv")
print("[2] Menu อ่าน pizzadata.txt")
menu = int(input("เลือก Menu : "))
if menu == 1:
    schooldata()
elif menu == 2:
    pizzadata()
