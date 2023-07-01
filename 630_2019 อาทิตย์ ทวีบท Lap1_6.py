#63_019 อาทิตย์ ทวีบท
import itertools as it 
A=[0,1]
listPnr = list(it.product(A,repeat=3))
print('เซตของเหตุการณ์\n',listPnr)
print('จำนวนวิธี=',len(listPnr),'วิธี')

A=['A','B','C']
B=list(range(10))
print(A)
print(B)

listPnr1=list(it.product(A,repeat=2))
print(listPnr1)
listPnr2=list(it.product(B,repeat=4))
print('จำนวนวิธี A=',len(listPnr1),'วิธี')
print('จำนวนวิธี B=',len(listPnr2),'วิธี')
print('จำนวนวิธี A&B=',len(listPnr1)*len(listPnr2),'วิธี')

#Ex1.25
A=[chr(i) for i in range(65,65+26)]
B=list(range(0,10))
n1=len(list(it.product(A,repeat=1)))
n21=n1
n22=len(list(it.product(A,repeat=1)))
n2=n21*n22
print('Ex1.25')
print(' จำนวนวิธี n1 =',n1,'วิธี')
print(' จำนวนวิธี n2 = n21 x n22 = %d x %d = %d วิธี'%(n21,n22,n2))
print(' จำนวนวิธี n = n1 + n2 = %d + %d = %d วิธี'%(n1,n2,n1+n2))

#Ex1.30
n=100
A=[str(x)for x in range(1,n+1)]
r=3
listPnr=list(it.permutations(A,r))
print('จำนวนวิธีตัวอย่าง 1.30 =',len(listPnr),'วิธี')

#Ex1.31
n=3
A=[str(x)for x in range(1,n+1)]
r=3
listPnr=list(it.permutations(A,r))
print('จำนวนวิธีตัวอย่าง 1.30 =',len(listPnr),'วิธี')
