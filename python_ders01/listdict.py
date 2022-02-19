# - Funksiya yazin parameter olaraq list,ve dict qebul etsin. Funksiya yoxlamalidi listin icindeki reqemler dictioneryde yoxdusa onlari silmelidi ve sonda listi return etmelidi. (mes : [27,22,34,44],{"tural": 27,"soltan": 22} funksiyaya gonderirsen o sene [27,22] qaytarir.
# a={} 
# b=['Monday','Tuesday','wednesday','Thursday','Friday','Saturday','Sunday']
# def func(l,d):
#     x=list(d)
#     for i in l:
#         if i==d[i]:
#             return True
#         else: 'Salam'
            
# func([27,22,34,44],{"tural": 27,"soltan": 22})       

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(type(x))
