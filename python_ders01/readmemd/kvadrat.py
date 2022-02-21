# Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.
kvadrat=[]
for i in range(4):
    b=int(input())
    kvadrat.append(b)
cevirme=set(kvadrat)
sifir=0
if len(cevirme)==1:
    
    for reqem in kvadrat:
        sahesi=sifir+reqem*reqem
    print(sahesi)
elif len(cevirme)>1:
    nope=0
    for sayi in kvadrat:
        nope=nope+sayi
    print(nope)

 