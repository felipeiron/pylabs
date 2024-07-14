import os
os.system('clear')

num_sum = 0
for i in range(0, 5):
    num_input = float(input('Send a number: '))
    num_sum += num_input

num_avg = num_sum / 5
print(f'Them SUM of this 5 numbers is {num_sum}. And the average is {num_avg}')