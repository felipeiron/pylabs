import os
os.system('clear')

print('### FIBONACCI ###')
fibo0 = 0
fibo1 = 1
while fibo1 < 500:
    print(fibo1, end=' ')
    fibo1 += fibo0
    fibo0 = fibo1 - fibo0
    if fibo1 > 500:
        print(fibo1)