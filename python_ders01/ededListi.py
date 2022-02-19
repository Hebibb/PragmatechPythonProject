
# reqemsayi=int(input())
# reqList=[]
# for i in range(reqemsayi):
#     myList=int(input())
#     reqList.append(myList)
# x=reqList.copy()
# reqList.reverse()
# print(x[0])
# print(reqList[0])
# print(type(x[0]))

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