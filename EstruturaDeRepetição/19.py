import os, random, time

set1 = []
while True:
    os.system('clear')
    print('### NUMERIC SETS ###\n')
    n_times = int(input('Enter the amount of number in the set: '))
    if n_times > 0 and n_times < 1000:
        for x in range(n_times):
            set1.append(random.randint(1, 999))
        else:
            set1 = sorted(set1)
            print('\n The set is: ', set1,'\n',
            'The biggiest valor is: ',set1[-1],'\n',
            'The shortiest valor is: ',set1[0],'\n',
            'The sum of all valors is: ',sum(set1),'\n'    
            )
            break
    else:
        print('\nThis number is invalid!')
        time.sleep(3)