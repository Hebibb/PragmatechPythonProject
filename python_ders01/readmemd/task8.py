# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
def func(listim):
    a=[]
    for string in listim:
        if string[0]==string[-1]:
            a.append(string)
    return len(a)
print(func(['abc', 'xyz', 'aba', '1221']))