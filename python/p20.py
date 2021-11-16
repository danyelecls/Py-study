s= float(input())

if s >=0 and s <=400:
    p= (0.15) 

if s >400 and s <=800:
    p= (0.12) 
    
if s >800 and s <=1200:
    p= (0.10)     
    
if s >1200 and s <=2000:
    p= (0.07)     
    
if s >2000:
    p= (0.04)     
    
r = s*p 
x = s + r

print('Novo salario:', f'{x :.2f}') 
print('Reajuste ganho:', f'{r:.2f}') 
print('Em percentual:', int(p*100), '%') 