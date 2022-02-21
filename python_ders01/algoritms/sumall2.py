# - Write a Python function to sum all the numbers in a list.
reqemsayi=int(input())
reqList=[]
for i in range(reqemsayi):
    myList=int(input())
    reqList.append(myList)
topla=0
for reqem in reqList:
    topla=topla+int(reqem)
print(topla)
