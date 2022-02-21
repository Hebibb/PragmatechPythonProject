dictionary={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
a=input()
b=a.split()
for i in b:
    if i in  dictionary:
        cavab=input(f'Do you mean {i}? ')
        if cavab=='yes':
            print(dictionary.get(i))
        elif cavab=='no':
            break
        else: print('Not founded')