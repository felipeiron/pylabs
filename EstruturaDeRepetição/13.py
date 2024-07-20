import os
os.system('clear')

num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))
i = 1
exp = 1

while i <= num2:
    exp *= num1
    i +=1

print(exp)