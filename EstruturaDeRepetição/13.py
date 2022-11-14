import os
os.system('clear')

print('### POWER OF ###\n')

power = [int(input('Enter the base: '))]
power.append(int(input('Enter the power: ')))
r_power = 1

for x in range(power[1]):
    r_power = r_power * power[0]
else:
    print(r_power)