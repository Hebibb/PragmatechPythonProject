# Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun. Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın. (İstədiyiniz qiyməti yazdırın). Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.


from meyveler import *
print(meyveler)
fruit=input()
testiq=bool(meyveler.get(fruit))


if testiq==True :
    print(f'{fruit}-in qiymeti {meyveler.get(fruit)} AZN-e beraberdi.')
else:print('^ERROR^')
