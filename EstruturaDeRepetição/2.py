import os

os.system('cls')

print('##### USER/PASSWORD #####\n')

while True:
    user = input('What is your username: ')
    passw = input('What is your password: ')
    if passw.upper() == user.upper():
        print('\nYour password cannot be the same as the username. ')
        print('Please, repeat the process!\n')
    else:
        break