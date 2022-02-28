want_amount=int(input())
besyuzlukler=int(want_amount/500)
ikiyuzluk=int((want_amount-besyuzlukler*500)/200)
yuzluk=int((want_amount-besyuzlukler*500-ikiyuzluk*200)/100)
ellilik=int((want_amount-besyuzlukler*500-ikiyuzluk*200-yuzluk*100)/50)
iyirmilik=int((want_amount-besyuzlukler*500-ikiyuzluk*200-yuzluk*100-ellilik*50)/20)
onluq=int((want_amount-besyuzlukler*500-ikiyuzluk*200-yuzluk*100-ellilik*50-iyirmilik*20)/10)

if want_amount%10==0:
    print(onluq+iyirmilik+ellilik+yuzluk+ikiyuzluk+besyuzlukler)





































    
 