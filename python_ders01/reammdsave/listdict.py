# Funksiya yazin parameter olaraq list,ve dict qebul etsin. Funksiya yoxlamalidi listin icindeki reqemler dictioneryde yoxdusa onlari silmelidi ve sonda listi return etmelidi. (mes : [27,22,34,44],{"tural": 27,"soltan": 22} funksiyaya gonderirsen o sene [27,22] qaytarir.
a={"tural": 27,"soltan": 22,'samir': 44}
b=[27,22,34,44]
def hesabla(listim,dictionary):
  topla=0
  if listim==list(listim) and dictionary== dict(dictionary):
    for i in listim:
      for j in dictionary:
        if i==dictionary.get(j):
         topla=topla+1
  else: return 'Melumati duzgun daxil edin'
  return topla

print(hesabla([12,35,99,103], {'soltan':99,'Qulam': 43,'Isfendiyar':12,'Kerbelayi':65,'sultan':103}))