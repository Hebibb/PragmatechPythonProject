val_coxalan=[10,20,50,100,200,500]
val_azalan=val_coxalan[::-1]
gel=[]

sifir=0

want_money=int(input())
qalan=want_money-i
for t in range(10):
    for i in val_azalan:
        want_money=qalan
        if want_money>0:
            gel.append(i)
            for j in val_azalan:
                want_money=qalan
                if want_money>0:
                    gel.append(j)
              
                else: break
        else: break
          
        
        
               

    
        
        

