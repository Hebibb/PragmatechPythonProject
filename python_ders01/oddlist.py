#  Write a Python program to select the odd items of a list.
reqemsayi=int(input())
reqList=[]
for i in range(reqemsayi):
    myList=int(input())
    reqList.append(myList)
print(reqList)
oddlist=[]
for odd in reqList:
    if int(odd)%2==1:
        oddlist.append(odd)
print(oddlist)