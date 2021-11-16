n = 0
m = 0
while n < 2:
    nota = float(input())
    if nota >= 0 and nota <= 10:
        n = n + 1
        m = m + nota
    if nota < 0 or nota > 10:
        print('nota invalida')
m = m / 2
print('media = {:.2f}'.format(m))