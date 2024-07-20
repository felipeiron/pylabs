import os
os.system('clear')

print('### FIBONACCI ###')
num = int(input('Enter a number: '))
fibo0 = 0
fibo1 = 1
for i in range(0, num):
    print(fibo1)
    fibo1 += fibo0
    fibo0 = fibo1 - fibo0