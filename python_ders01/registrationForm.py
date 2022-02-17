ad=input('Adiniz: ')
adlength=len(ad)
    
if adlength > 3 and adlength < 11:
    soyad=input('Soyadiniz: ')
    if len(soyad)>5 and len(soyad)<15:
        il=input('Doguldugunuz il: ')
        if len(il)==4:
            email=input('Emailinizi daxil edin:')
            gmail='@gmail.com'
            if bool(email.endswith(gmail))==True and len(email)>10 and len(email)<22:
                password=input('passwordunuzu daxil edin: ')
                if len(password)>6 and len(password)<13:
                    testiq=input('passwordunuz tekrarlayin: ')
                    if testiq==password:
                        print(f'ad:{ad}, soyad: {soyad}, dogum ili: {il}, email: {email}, password: {password} ')
                    else: print(f'Ugurlar {ad} {soyad}!')
                else: print('passwordun simvol sayi 6-dan boyuk 11 den kicik olmalidir')
                             
            else: print(f'Email melumatinin sonunda {gmail} hissesi yoxdur.')
        else: print(f'Daxil etdiyiniz ilin reqem sayi 4-den ferqli olabilmez')
    else: print('Userin soyadi 5-den kicik veya 15 boyuk olabilmez.')
else: print('Userin adi 3-den kicik veya 11 boyuk olabilmez.')
    