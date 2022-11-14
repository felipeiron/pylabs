import os

os.system('clear')
l_num = []
print('### THE BIGGEST NUMBER ###\n')
for x in range(5):
    l_num.append(int(input('Enter a number: ')))
else:
    l_num = sorted(l_num)
    print('\nThe biggest number is', l_num[4],'\n')