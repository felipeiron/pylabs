import os, time

fat = 1
while True:
    os.system('clear')
    print('### FACTORIAL ###\n')
    num = int(input('Please, enter a integer: '))
    if num > 0 and num < 16:
        for x in range(num):
            fat = fat * (num - x)
        else:
            print(fat)
            break
    else:
        print('This number is invalid!')
        time.sleep(3)