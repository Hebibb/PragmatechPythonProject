from meyveler import *
print(meyveler)
fruit=input()
testiq=bool(meyveler.get(fruit))


if testiq==True :
    print(f'{fruit}-in qiymeti {meyveler.get(fruit)} AZN-e beraberdi.')
else:print('^ERROR^')
