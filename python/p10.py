nome = input()
s =  float(input())
v =  float(input())

comissao = float(v * (15/100))
t = s + comissao

print("TOTAL = R$ %0.2f" %t)