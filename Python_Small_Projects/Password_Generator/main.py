"""
Password Generator in Python
"""

import random
print('Your Password: ')

#all possible characters
chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[]{}|;:'"<,>.?/`~"

# declare password as an empty string.
password = ''

# for x in range, password is set to chose randoms characters
for x in range(16):
    password = random.choice(chars)

    print(password)
