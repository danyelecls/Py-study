v = int(input())

c = [100, 50, 20, 10, 5, 2 , 1]

print(v)

for c in c:
  qC = int(v / c)
  print("{} nota(s) de R$ {},00".format(qC, c))
  v -= qC * c