#  funksiya yazin ededlerden ibaret list qebul etsin ve eger listin birinci ve sonuncu elementleri beraberdise return True qaytarsin. Mes: [1,2,3,1] bu halda True qaytaracag

def reverseit():
    reqemsayi=int(input())
    reqList=[]

    for i in range(reqemsayi):
        myList=int(input())
        reqList.append(myList)
  
    if reqList[0]==reqList[-1]:
        return True
    else: return False


print(reverseit())