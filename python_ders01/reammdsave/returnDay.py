# Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and returns the day of the week ( 1 is Sunday, 2 is Monday etc.). If the number is less than 1 or greater than 7, the function should return None.

def returnDay(gun):
    if gun>1 and gun<8:
        gunler=['Monday','Tuesday','Wednesday','Thirsday','Friday','Saturday','Sunday']
        a=f'{gun} is {gunler[gun]}'
        return a
    else: return None
print(returnDay(6))