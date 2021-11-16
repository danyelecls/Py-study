v= input()

c, q= v.split(' ')

c= int(c)
q= int(q)

if c == 1:
    p = 4.00
    
if c == 2:
    p = 4.50
    
if c == 3:
    p =5.00
    
if c == 4:
    p =2.00
    
if c == 5:
    p =1.50  

total= q*p
print('Total: R$', f'{(total):.2f}') 