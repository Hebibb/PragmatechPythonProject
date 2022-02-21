#  Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website.
#  Loop through the list, and print a greeting to each user: • If the username is 'admin' , print a special greeting, such as Hello admin, would you like to see a status report? • 
# Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
salam=['Samir','Gulab','admin','Gulabatin']
for i in salam:
    if i=='admin':
        print(f'Xususi salamlar {i}-e')
    else: print(f'Salamlar {i} ')