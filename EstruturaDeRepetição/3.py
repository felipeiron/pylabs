import os
import time

os.system('clear')

print('### FORM ###')

while True:
    name = input('Your name: ')
    age = int(input('Your age: '))
    wage = float(input('Your wage: '))
    genre = input('Your genre: ')
    marital_s = input('Your marital status: ')
    if len(name) < 3:
        print('Invalid!')
    elif age < 0 or age > 150:
        print('Invalid!')
    elif wage <= 0:
        print('Invalid!')
    elif genre != 'f' and genre != 'm':
        print('Invalid!')
    elif marital_s != 's' and marital_s != 'c' and marital_s != 'v' and marital_s != 'd':
        print('Invalid!')
    else:
        break