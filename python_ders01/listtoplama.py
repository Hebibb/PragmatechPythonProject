l_sira=int(input('neqeder reqem daxil edeceksiniz? '))
reqemler=[]
for i in range(l_sira):
    i=input()
    reqemler.append(i)
toplu=0
for say in reqemler:
    toplu=toplu+int(say)
print(toplu)
