# a=54.23
# print(int(a+1))

siparis=int(input())
if siparis<1000:
    for i in range(siparis):
        l=int(input())
        w=int(input())
        h=int(input())
        sahesi=l*w*h
        rengleme=sahesi/2
        banka=16
        istifade=round(rengleme/banka)
        if type(istifade)==float:
            istifade=istifade+1
            print(f'{i+1} nomreli siparis ucun {istifade}  banka istifade olunacaq')
        print(f'{i+1} nomreli siparis ucun {istifade}  banka istifade olunacaq')
else: print('siparisleri catdirmaq mumkun deyil')