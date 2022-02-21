# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
a=input()
b=list(a)
listim=['abc', 'xyz', 'aba', '1221'] 
for i in b:
    if len(a)>=2 and b[0]==listim:
        print(a)