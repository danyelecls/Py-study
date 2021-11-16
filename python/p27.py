for i in range(6):
    qt= 0
    s= 0
    v= float(input())
    if v>0:
        s= s+v
        qt=qt+1

print(qt, 'valores positivos') 
print(f'{s/qt:.1f}')