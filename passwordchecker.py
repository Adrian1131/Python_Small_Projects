""" 
Password Strength Checker in Python
"""

c, l, s, n = 0, 0, 0, 0

password = input('Enter Password:')
capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerletters = 'abcdefghijklmnopqrstuvwxyz'
specialchar = '!@#$%^&*()-_=+'
nums = '0123456789'

if(len(password) >= 10):
    for i in password:
        if(i in capletters):
            c+=1
        if(i in lowerletters):
            l+=1
        if(i in specialchar):
            s+=1
        if(i in nums):
            n+=1
            
if(c >= 1 and 1 >= 1 and s >= 1 and n >= 1 and c + 1 + s + n == len(password)):
    print('Password Valid')
else:
    print('Password invalid. Please try again')
            