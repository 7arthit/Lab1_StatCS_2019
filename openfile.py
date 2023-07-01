with open("test2.txt") as in_fi:
    lines = in_fi.read()
    print(lines)
        
with open("test2.csv", encoding='utf-8') as file:
    for lines in file:
        txt=lines.split(',')
        print(txt[0],txt[1],txt[2])
        
with open("test2.txt") as in_fi:
    lines = in_fi.read()
    print(lines)
    for l in lines:
        print(l)

with open("test2.txt", encoding='utf-8') as file:
    print(file)
    for lines in file:
        txt2=lines.split('\n')
        print(txt2)
        txt3=txt2[0].split('\t')
        print(txt3)
