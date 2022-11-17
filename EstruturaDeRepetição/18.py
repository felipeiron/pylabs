import os, random
os.system('clear')

print('### NUMERIC SETS ###\n')

n_times = int(input('Enter the amount of number in the set: '))
set1 = []
for x in range(n_times):
    set1.append(random.randint(1, 999))
else:
    set1 = sorted(set1)
    print(' The set is: ', set1,'\n',
    'The biggiest valor is: ',set1[-1],'\n',
    'The shortiest valor is: ',set1[0],'\n',
    'The sum of all valors is: ',sum(set1)    
    )