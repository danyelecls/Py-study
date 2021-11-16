hi, hf = list(map(int,input().split()))

if(hi<hf):
    t=hf-hi
else:
    t=hf+24-hi
print(f"O JOGO DUROU {t} HORA(S)")