import os
os.system('clear')

print('### FIBONACCI ###\n')

fibo = [1,1]
last_fibo = int(input('Enter the last position of Fibonacci sequency: '))

for i in range(2, last_fibo):
    fibo.append(fibo[i-1]+fibo[i-2])
else:
    print(fibo)
