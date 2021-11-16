l1= input().split()
c1= int(l1[0])
n1= int(l1[1])
v1= float(l1[2])

l2= input().split()
c2= int(l2[0])
n2= int(l2[1])
v2= float(l2[2])

total=n1*v1+n2*v2
print('VALOR A PAGAR: R$', f'{(total):.2f}')