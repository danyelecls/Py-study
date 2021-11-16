hi,mi,hf,mf=list(map(int,input().split()))

x=((hf*60)+mf)-((hi*60)+mi)
if(x<=0):
    x+=24*60
    
t=x//60
m=x%60
print(f"O JOGO DUROU {t} HORA(S) E {m} MINUTO(S)")