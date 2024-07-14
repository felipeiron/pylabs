import os
os.system('clear')

num1 = int(input('Enter a integer number: '))
num2 = int(input('Enter another integer number: '))

if num2 > num1:
    num1 += 1
    for i in range(num1, num2):
        print(i, end=' ')
elif num1 > num2:
    num2 += 1
    for i in range(num2, num1):
        print(i, end=' ')
else:
    print('The numbers are equal')

print(f'<== This is the integer number between {num1} and {num2}!')