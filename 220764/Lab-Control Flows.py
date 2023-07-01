#while example
print('While example')
i=1
while i <=20:
    if i%2==0:
        print(i)
    i+=1

#for example
print('For example')
for i in range(20):
    if i%2==1:
        print(i)
#3
score=float(input('Input score:'))
if score<0:
    print('Error')
elif score>=80:
    print('Score=%.2f, Grade=A'% score)
elif score>=70:
    print('Score=%.2f, Grade=B'% score)
elif score>=60:
    print('Score=%.2f, Grade=C'% score)
elif score>=50:
    print('Score=%.2f, Grade=D'% score)
else:
    print('Score=.2f, Grade=F'% score)
