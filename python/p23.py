s = float(input()) 
i = 0
    

if s >2000 and s <=3000: 
   s8 = s - 2000.00
   i = s8 * (8 / 100)
   print('R$ {:.2f}'.format(i))
    
if s > 3000 and s <=4500: 
    i8 = (8 / 100) * (1000.00)
    s18 = s - 3000.00
    i = s18 * (18 / 100) + i8
    print('R$ {:.2f}'.format(i))
    
if s > 4500:
    i8 = (8 / 100) * (1000.00)
    i18 = (18 / 100) * (1500.00)
    s28 = s - 4500.00
    i = i18 + i8 + s28 * (28 / 100)
    print('R$ {:.2f}'.format(i))

if s <= 2000.00:
    print('Isento')
    
