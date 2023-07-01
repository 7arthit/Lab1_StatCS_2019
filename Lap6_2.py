#63_2019 อาทิตย์ ทวีบท Lab6_2
import itertools as it

#การจัดหมู่(Combination)
#Ex1.36
A=[0,1]
r=7
listCnr=list(it.combinations_with_replacement(A,r))
print('จำนวนวิธีตัวอย่าง 1.36 =',len(listCnr),'วิธี')

#Ex1.37
A='abcd'
r=2
listCnr=list(it.combinations(A,r))
print('จำนวนวิธีตัวอย่าง 1.37 =',len(listCnr),'วิธี')

#Ex1.38
A=list(range(1,11))
r=5
listCnr=list(it.combinations(A,r))
print('จำนวนวิธีตัวอย่าง 1.38 =',len(listCnr),'วิธี')

#Ex1.39
A=list(range(1,31))
r=6
listCnr=list(it.combinations(A,r))
print('จำนวนวิธีตัวอย่าง 1.39 =',len(listCnr),'วิธี')

#Ex1.40
A=list(range(1,10))
B=list(range(1,12))
rA=3
rB=4
nA=len(list(it.combinations(A,rA)))
nB=len(list(it.combinations(A,rB)))
print('จำนวนวิธีตัวอย่าง 1.34 = nA x nB = %d x %d = %d วิธี'%(nA,nB,nA*nB))

#Probability
#Ex2.1
S=list(range(1,10))
nS=len(list(it.combinations(S,1)))
nE=len(list(it.combinations(list(range(1,5)),1)))
p=nE/float(nS)
print('จำนวนวิธีของ S = ',nS,',จำนวนวิธีของ E = ',nE)
print('ความน่าจะเป็น = ',p)
print('ความน่าจะเป็น  = %.4f'%p)

#Ex2.9
A=list(range(10))
nA=list(it.product(A,repeat=4))
print('จำนวนวิธี = ',len(nA))
