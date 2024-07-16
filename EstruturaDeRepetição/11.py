import os
os.system('clear')

num1 = int(input('Enter a integer number: '))
num2 = int(input('Enter another integer number: '))
num_sum = 0

if num2 > num1:
    num1 += 1
    for i in range(num1, num2):
        num_sum += i
        print(i, end=' ')
        
    print(f'<== This is the integer number between {num1} and {num2}. The SUM is {num_sum}!')
elif num1 > num2:
    num2 += 1
    for i in range(num2, num1):
        num_sum += i
        print(i, end=' ')

    print(f'<== This is the integer number between {num1} and {num2}. The SUM is {num_sum}!')
else:
    print('The numbers are equal')