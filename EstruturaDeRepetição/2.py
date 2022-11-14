import os, time

while True:
    os.system('clear')
    print('##### USER/PASSWORD #####\n')
    user = input('What is your username: ')
    passw = input('What is your password: ')
    if passw.upper() == user.upper():
        print('\nYour password cannot be the same as the username. ')
        print('Please, repeat the process!\n')
        time.sleep(3)
    else:
        print('\nProcess finished!\n')
        break